from django.shortcuts import render
from .models import Empleado
from django.views.generic import (
    TemplateView,
    ListView
    )

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class ListAllEmpleadosView(ListView):
    template_name = "persona/list_all.html"
    model = Empleado
    context_object_name = 'lista'

class ListByAreaEmpleadosView(ListView):
    template_name = "persona/list_by_area.html"

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(departamento__name=area)
        return lista
