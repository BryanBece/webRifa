from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nombre', 'telefono', 'email')
    search_fields = ('numero', 'nombre', 'telefono', 'email')
    list_filter = ('nombre', 'telefono')
    ordering = ('numero',)