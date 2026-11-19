from django import forms
from apps.adopcion.models import Persona, Solicitud

class PersonaForm (forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellidos',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'telefono' : 'Telefono',
            'email' : 'Email',
            'domicilio' : 'Domicilio',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
            'apellidos' : forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
            'edad': forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
            'telefono' : forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
            'email' : forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
            'domicilio':  forms.TextInput(attrs={'class' : 'form-control','required':True}),
        }
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
        #     'apellidos' : forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
        #     'edad': forms.NumberInput(attrs={'class' : 'form-control', 'required':True}),
        #     'telefono' : forms.NumberInput(attrs={'class' : 'form-control', 'required':True}),
        #     'email' : forms.EmailInput(attrs={'class' : 'form-control', 'required':True}),
        #     'domicilio':  forms.TextInput(attrs={'class' : 'form-control', 'required':True}),
        # }

class Solicitudform (forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas': 'Numero de mascotas',
            'razones' : 'Razones para adoptar',
        }
        widgets = {
            'numero_mascotas' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'razones' : forms.TextInput(attrs={'class' : 'form-control'}),
        }