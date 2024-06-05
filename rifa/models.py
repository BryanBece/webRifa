from django.db import models

# Create your models here.

class Ticket(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Ticket {self.numero} - {self.nombre}"