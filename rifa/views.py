# rifa/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import TicketForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def home(request):
    total_numbers = 125
    tickets = Ticket.objects.all()
    taken_numbers = {ticket.numero for ticket in tickets}
    numbers = [{'number': i, 'available': i not in taken_numbers} for i in range(1, total_numbers + 1)]
    return render(request, 'rifa/home.html', {'numbers': numbers})

def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'rifa/ticket_detail.html', {'ticket': ticket})

def add_ticket(request, numero):
    if Ticket.objects.filter(numero=numero).exists():
        messages.error(request, '¡El ticket ya está reservado!')
        return redirect('home')

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
            messages.success(request, '¡Ticket agregado exitosamente!')
            return redirect('home')
    else:
        form = TicketForm(initial={'numero': numero})

    return render(request, 'rifa/add_ticket.html', {'form': form, 'numero': numero})

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    messages.success(request, '¡Ticket eliminado exitosamente!')
    return redirect('home')

@login_required
def profile(request):
    tickets = Ticket.objects.all()
    return render(request, 'rifa/profile.html', {'tickets': tickets})

@login_required
def logout(request):
    auth.logout(request)
    return redirect("home")


def update_ticket(request, ticket_id):
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        ticket.pagado = not ticket.pagado
        ticket.save()
        return JsonResponse({'status': 'success', 'pagado': ticket.pagado})
    return JsonResponse({'status': 'error'}, status=400)

def tickets_pdf(request):
    # Trae TODOS los registros (sin paginar ni cortar)
    tickets = Ticket.objects.order_by('numero')

    # Renderiza el HTML de la plantilla de PDF
    template = get_template('rifa/tickets_pdf.html')
    html = template.render({'tickets': tickets})

    # Prepara la respuesta como PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="tickets.pdf"'

    # Genera el PDF
    pisa_status = pisa.CreatePDF(html, dest=response, encoding='utf-8')

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF.', status=500)

    return response