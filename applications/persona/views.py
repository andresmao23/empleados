from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Empleado
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class ListAllEmpleadosView(ListView):
    template_name = "persona/list_all.html"
    model = Empleado
    paginate_by = 4
    context_object_name = 'lista'

class ListByAreaEmpleadosView(ListView):
    template_name = "persona/list_by_area.html"

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(departamento__name=area)
        return lista

class BuscarEmpleadoByKwordView(ListView):
    template_name = "persona/buscar_empleado.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(last_name=palabra_clave)
        return lista

class EmpleadoDetailView(DetailView):
    template_name = 'persona/detail_empleado.html'
    model = Empleado
    context_object_name = 'empleado'

class SuccessView(TemplateView):
    template_name = 'persona/success.html'

class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('persona:success')

class SuccessUpdateView(TemplateView):
    template_name = 'persona/update-success.html'

class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = ('__all__')
    success_url = reverse_lazy('persona:update-success')

class SuccessDeleteUpdateView(TemplateView):
    template_name = 'persona/delete-success.html'

class EmpleadoDeleteView(DeleteView):
    template_name = 'persona/delete.html'
    model = Empleado
    success_url = reverse_lazy('persona:empleado-delete-success')
