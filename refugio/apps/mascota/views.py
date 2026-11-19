from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from apps.mascota.forms import MascotaForm, VacunasForm
from apps.mascota.models import Mascotas2, Vacunas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

incorrecto = 'Por favor llena correctamente los campos'
# Create your views here.
## Vista por funciones Mascota -----------------------------------
def index(request):
    return render(request, 'mascota/index.html')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nombre_mascota = form.cleaned_data['nombre']
            messages.success(request, 'La mascota %s se creo correctamente' %nombre_mascota, extra_tags='alert-success')
            return redirect('mascota:mascota_listar')
        else:
           messages.error(request,incorrecto , extra_tags='alert-warning') 
    else:
        form = MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form':form})


def mascota_list(request):
    mascota = Mascotas2.objects.all().order_by('id')
    contexto = {'mascotas' : mascota}
    return render(request, 'mascota/mascota_list.html', contexto)


def mascota_edit(request, id_mascota):
    mascota = Mascotas2.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else: 
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, 'La mascota %s se edito correctamente'%mascota.nombre, extra_tags='alert-success')
            return redirect('mascota:mascota_listar')
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
    return render(request, 'mascota/mascota_form.html', {'form':form})


def mascota_delete(request, id_mascota):
    mascota = Mascotas2.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        messages.success(request, 'La mascota %s se elimino correctamente'%mascota.nombre, extra_tags='alert-success')
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})


## Vista por funciones Vacuna -----------------------------------
def vacuna_view(request):
    if request.method == 'POST':
        form = VacunasForm(request.POST)
        if form.is_valid():
            form.save()
            nombre_vacuna = form.cleaned_data['nombre']
            print('IMPRIMIR A ', {nombre_vacuna})
            messages.success(request, 'La vacuna %s fue creada correctamente'%nombre_vacuna, extra_tags='alert-success')
            return redirect('mascota:vacuna_listar')
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
            
    else:
        form = VacunasForm()
    return render(request,'mascota/vacuna_form.html', {'form':form} )


def vacuna_list(request):
    vacuna = Vacunas.objects.all().order_by('id')
    contexto = {'vacunas': vacuna}
    return render(request, 'mascota/vacuna_list.html', contexto)


def vacuna_edit(request, id_vacuna):
    vacuna = Vacunas.objects.get(id = id_vacuna)
    if request.method == 'GET':
        form = VacunasForm(instance=vacuna)
    else:
        form = VacunasForm(request.POST, instance=vacuna)
        if form.is_valid():
            form.save()
            # nombre_vacuna = form.cleaned_data['nombre']
            # print('IMPRIMIR ESTO ', {vacuna.nombre})
            # messages.success(request, 'La vacuna %s se edito correctamente'%nombre_vacuna, extra_tags='alert-success')
            messages.success(request, 'La vacuna %s se edito correctamente'%vacuna.nombre, extra_tags='alert-success')
            return redirect ('mascota:vacuna_listar')
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
    return render(request, 'mascota/vacuna_form.html', {'form':form})


def vacuna_delete(request, id_vacuna):
    vacuna = Vacunas.objects.get(id = id_vacuna)
    if request.method == 'POST':
        vacuna.delete()
        print('IMPRIMIR A ', {vacuna.nombre})
        messages.success(request, 'La vacuna %s se elimino correctamente'%vacuna.nombre, extra_tags='alert-success')
        return redirect ('mascota:vacuna_listar')       
    return render (request, 'mascota/vacuna_delete.html', {'vacuna' : vacuna})

## Vista por clases Mascota -----------------------------------
class MascotaList(ListView):
    model = Mascotas2
    template_name = 'mascota/mascota_list_clases.html'

class MascotaCreate(CreateView):
    model = Mascotas2
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar_clases')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save()
            nombre_mascota = form.cleaned_data['nombre']
            print('IMPRIMIR',mascota.nombre)
            messages.success(request, 'La mascota %s se creo correctamente'%nombre_mascota, extra_tags='alert-success')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
            return self.render_to_response(self.get_context_data(form = form))

class MascotaUpdate(UpdateView):
    model = Mascotas2
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar_clases')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_mascota = kwargs['pk']
        mascota = self.model.objects.get(id = id_mascota)
        form = self.form_class(request.POST, request.FILES, instance = mascota)
        if form.is_valid():
            form.save()
            messages.success(request, 'La mascota %s se edito correctamente'%mascota.nombre, extra_tags='alert-success')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
            return self.render_to_response(self.get_context_data(form = form))

class MascotaDelete(SuccessMessageMixin, DeleteView):
    model = Mascotas2
    template_name = 'mascota/mascota_delete_clases.html'
    success_url = reverse_lazy('mascota:mascota_listar_clases')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, 'La mascota %s se elimino correctamente'%self.object.nombre, extra_tags='alert-success')
        return super().delete(request, *args, **kwargs)


# class MascotaDelete(DeleteView):
#     model = Mascotas2
#     template_name = 'mascota/mascota_delete_clases.html'
#     success_url = reverse_lazy('mascota:mascota_listar_clases')
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object
#         id_mascota = kwargs['pk']
#         mascota = self.model.objects.get(id = id_mascota)
#         if request.method == 'POST':
#             mascota.delete()
#             messages.success(request, 'Las mascota %s se elimino correctamente'%mascota.nombre, extra_tags='alert-success')
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(mascota = mascota))

## Vista por clases Mascota -----------------------------------
class VacunaList (ListView):
    model = Vacunas
    template_name = 'mascota/vacuna_list_clases.html'
    
class VacunaCreate(SuccessMessageMixin, CreateView):
    model = Vacunas
    form_class = VacunasForm
    template_name = 'mascota/vacuna_form.html'
    success_url = reverse_lazy('mascota:vacuna_listar_clases')
    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'La vacuna %s se creo correctamente'%self.object.nombre, extra_tags='alert-success')
    def form_invalid(self, form):
        messages.error(self.request, incorrecto, extra_tags='alert-warning')
        return super().form_invalid(form)


# class VacunaCreate(CreateView, SuccessMessageMixin):
#     model = Vacunas
#     form_class = VacunasForm
#     template_name = 'mascota/vacuna_form.html'
#     success_url = reverse_lazy('mascota:vacuna_listar_clases')
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             nombre_vacuna = form.cleaned_data['nombre']
#             messages.success(request, 'La vacuna %s se creo correctamente'%nombre_vacuna, extra_tags='alert-success')
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             messages.error(request, incorrecto, extra_tags='alert-warning')
#             return self.render_to_response(self.get_context_data(form = form))

class VacunaUpdate(SuccessMessageMixin, UpdateView):
    model = Vacunas
    form_class = VacunasForm
    template_name = 'mascota/vacuna_form.html'
    success_url = reverse_lazy('mascota:vacuna_listar_clases')
    def get_success_message(self, cleaned_data):
        return messages.success(self.request, 'La vacuna %s se modifico correctamente'%self.object.nombre, extra_tags='alert-success')
    def form_invalid(self, form):
        messages.error(self.request, incorrecto, extra_tags='alert-warning')
        return super().form_invalid(form)


# class VacunaUpdate(UpdateView):
#     model = Vacunas
#     form_class = VacunasForm
#     template_name = 'mascota/vacuna_form.html'
#     success_url = reverse_lazy('mascota:vacuna_listar_clases')
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object
#         id_vacuna = kwargs['pk']
#         vacuna = self.model.objects.get(id = id_vacuna)
#         form = self.form_class(request.POST, instance = vacuna)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'La vacuna %s se edito correctamente' %vacuna.nombre, extra_tags='alert-success')
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return HttpResponseRedirect(self.get_success_url())

class VacunaDelete(DeleteView):
    model = Vacunas
    template_name = 'mascota/vacuna_delete_clases.html'
    success_url = reverse_lazy('mascota:vacuna_listar_clases')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_vacuna = kwargs['pk']
        vacuna = self.model.objects.get(id = id_vacuna)
        if request.method == 'POST':
            vacuna.delete()
            messages.success(request, 'La vacuna %s se elimino correctamente'%vacuna.nombre, extra_tags='alert-success')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(vacuna = vacuna))