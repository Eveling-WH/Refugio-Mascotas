from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, Solicitudform
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


incorrecto = 'Por favor llena correctamente los campos'

## Vista por funciones aopcion -----------------------------------
def index_adopcion(request):
    return HttpResponse("Pagina principal de la app adopcion")

def adoptante_view(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            nombre_adoptante = form.cleaned_data['nombre']
            messages.success(request, 'El adoptante %s se creo correctamente'%nombre_adoptante, extra_tags='alert-success')
            return redirect('adopcion:adoptante_listar')
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
    else:
        form = PersonaForm()
    return render(request, 'adopcion/adoptante_form.html',{'form':form})


def adoptante_list(request):
    adoptante = Persona.objects.all().order_by('id')
    contexto = {'persona': adoptante}
    return render(request, 'adopcion/adoptante_list.html', contexto)

def adoptante_edit(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'GET':
        form = PersonaForm(instance=persona)
    else:
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, 'El adoptante %s se edito correctamente'%persona.nombre, extra_tags='alert-success')
            return redirect ('adopcion:adoptante_listar')
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
    return render(request, 'adopcion/adoptante_form.html', {'form':form})

def adoptante_delete(request, id_persona):
    persona = Persona.objects.get(id=id_persona)
    if request.method == 'POST':
        persona.delete()
        messages.success(request, 'El adoptante %s se elimino correctamente'%persona.nombre, extra_tags='alert-success')
        return redirect('adopcion:adoptante_listar')
    return render(request, 'adopcion/adoptante_delete.html', {'persona':persona})

## Vista por clases Adopcion -----------------------------------
class AdoptanteList(ListView):
    model = Persona
    template_name = 'adopcion/adoptante_list_clases.html'

class AdoptanteCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'adopcion/adoptante_form.html'
    success_url = reverse_lazy('adopcion:adoptante_listar_clases')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            nombre_adoptante = form.cleaned_data['nombre']
            messages.success(request, 'El adoptante %s se creo correctamente'%nombre_adoptante, extra_tags='alert-success')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
            return self.render_to_response(self.get_context_data(form = form))

class AdoptamteUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'adopcion/adoptante_form.html'
    success_url = reverse_lazy('adopcion:adoptante_listar_clases')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_adoptante = kwargs['pk']
        adoptante = self.model.objects.get(id = id_adoptante)
        form = self.form_class(request.POST, request.FILES, instance = adoptante)
        if form.is_valid():
            form.save()
            messages.success(request, 'El adoptante %s se edito correctamente'%adoptante.nombre, extra_tags='alert-success')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
            return self.render_to_response(self.get_context_data(form = form))

class AdoptanteDelete(DeleteView):
    model = Persona
    template_name = 'adopcion/adoptante_delete_clases.html'
    success_url = reverse_lazy('adopcion:adoptante_listar_clases')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_adoptante = kwargs['pk']
        adoptante = self.model.objects.get(id = id_adoptante)
        if request.method == 'POST':
            adoptante.delete()
            messages.success(request, 'El adoptante %s se elimino correctamente'%adoptante.nombre, extra_tags='alert-success')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(adoptante = adoptante))


## Vista por clases Solicitud -----------------------------------
class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list_clases.html'

class SolicitudCreate(CreateView):
    model = Solicitud
    form_class = Solicitudform
    second_form_class = PersonaForm
    template_name = 'adopcion/solicitud_form.html'
    success_url = reverse_lazy('adopcion:solicitud_listar_clases')
    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        # context = (SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
            ## Formulario 1
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            ## Formulario 2
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit = False)
            solicitud.persona = form2.save()
            solicitud.save()
            messages.success(request, 'Las solicitud de %s se creo correctamente'%solicitud.persona.nombre, extra_tags='alert-success')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/solicitud_form.html'
    form_class = Solicitudform
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:solicitud_listar_clases')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id = id_solicitud)
        persona = self.second_model.objects.get(id = solicitud.persona_id)
        form = self.form_class(request.POST, instance = solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, 'Las solicitud de %s se edito correctamente'%solicitud.persona.nombre, extra_tags='alert-success')
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
            return self.render_to_response(self.get_context_data(form = form, form2 = form2))

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/solicitud_delete_clases.html'
    success_url = reverse_lazy('adopcion:solicitud_listar_clases')

## Vista por funciones Solicitud -----------------------------------
def solicitud_list(request):
    solicitud = Solicitud.objects.all().order_by('id')
    contexto = {'solicitudes': solicitud}
    return render(request, 'adopcion/solicitud_list.html', contexto)

def solicitud_view(request):
    if request.method == 'POST':
        form = Solicitudform(request.POST)
        form2 = PersonaForm(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save()
            solicitud.persona = form2.save()
            solicitud.save()
            messages.success(request, 'La solicitud de %s se creo correctamente'%solicitud.persona.nombre, extra_tags='alert-success')
            return redirect('adopcion:solicitud_listar')
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
    else:
        form = Solicitudform()
        form2 = PersonaForm()
    return render(request, 'adopcion/solicitud_form.html',{'form':form, 'form2':form2})

def solicitud_delete(request, id_solicitud):
    solicitud = Solicitud.objects.get(id = id_solicitud)
    if request.method == 'POST':
        solicitud.delete()
        messages.success(request, 'La solicitud de %s se elimino correctamente'%solicitud.persona.nombre, extra_tags='alert-success')
        return redirect('adopcion:solicitud_listar')
    return render(request, 'adopcion/solicitud_delete.html', {'solicitud':solicitud})

def solicitud_edit(request, id_solicitud):
    solicitud = Solicitud.objects.get(id = id_solicitud)
    persona = Persona.objects.get(id = solicitud.persona_id)
    if request.method == 'GET':
        form = Solicitudform(instance=solicitud)
        form2 = PersonaForm(instance=persona)
    else:
        form = Solicitudform(request.POST, instance = solicitud)
        form2 = PersonaForm(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, 'La solicitud de %s se edito correctamente'%persona.nombre, extra_tags='alert-success')
            return redirect ('adopcion:solicitud_listar')
        else:
            messages.error(request, incorrecto, extra_tags='alert-warning')
    return render(request, 'adopcion/solicitud_form.html', {'form':form, 'form2':form2})