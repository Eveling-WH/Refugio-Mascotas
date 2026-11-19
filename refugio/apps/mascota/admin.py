from django.contrib import admin
from apps.mascota.models import Vacunas, Mascotas2 ## Se importa por el nombre de la carpeta a la que pertenece y el nombre del modelo
# Register your models here.
admin.site.register(Vacunas)
admin.site.register(Mascotas2)