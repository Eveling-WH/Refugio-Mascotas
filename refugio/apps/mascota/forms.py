from django import forms
from apps.mascota.models import Mascotas2, Vacunas

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascotas2

        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
            'imagen',
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo' : 'Sexo',
            'edad_aproximada' : 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona' : 'Adoptante',
            'vacuna' : 'Vacuna',
            'imagen' : 'Imagen',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'sexo': forms.TextInput(attrs={'class' : 'form-control'}),
            'edad_aproximada' : forms.TextInput(attrs={'class' : 'form-control'}),
            'fecha_rescate': forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            'persona' : forms.Select(attrs={'class' : 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),            
        }

        # widgets = {
        #     'nombre' : forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
        #     'sexo': forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
        #     'edad_aproximada' : forms.NumberInput(attrs={'class' : 'form-control', 'required':True}),
        #     'fecha_rescate': forms.DateInput(format="%Y-%m-%d", attrs={"type": "date", 'required':True}),
        #     'persona' : forms.Select(attrs={'class' : 'form-control', 'required':True}),
        #     'vacuna': forms.CheckboxSelectMultiple(),            
        # }
        

class VacunasForm(forms.ModelForm):
    class Meta:
        model = Vacunas
        fields = [
            'nombre',
        ]
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre' : forms.TextInput( attrs={'class' : 'form-control'}),
        }