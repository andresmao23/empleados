from django.shortcuts import render
from .models import Empleado
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
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

