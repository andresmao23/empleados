from django.urls import path
from .views import (
    IndexView,
    ListAllEmpleadosView,
    ListByAreaEmpleadosView,
    BuscarEmpleadoByKwordView,
    EmpleadoDetailView
    )

app_name = 'persona'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list-all-empleados/', ListAllEmpleadosView.as_view(), name='list-all'),
    path('list-by-area/<name>/', ListByAreaEmpleadosView.as_view(), name='list-by-area'),
    path('buscar-empleado/', BuscarEmpleadoByKwordView.as_view(), name='buscar-empleado'),
    path('detail-empleado/<pk>/', EmpleadoDetailView.as_view(), name='detail-empleado'),
]
