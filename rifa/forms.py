# rifa/forms.py
from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['numero', 'nombre', 'telefono', 'email']
        widgets = {
            'numero': forms.NumberInput(attrs={'readonly': 'readonly', 'placeholder': 'Número del Ticket'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese Nombre'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese Teléfono'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese Correo Electrónico (opcional)'}),
        }
