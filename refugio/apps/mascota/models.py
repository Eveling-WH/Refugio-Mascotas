from django.db import models
from apps.adopcion.models import Persona

class Vacunas(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nombre)


class Mascotas2(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada =  models.IntegerField() ##Los enteros no reciben un max length
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacunas, blank=True)
    imagen = models.ImageField(blank=True)

    def __str__(self):
            return '{}'.format(self.nombre)