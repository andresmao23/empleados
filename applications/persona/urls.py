from django.urls import path
from .views import (
    IndexView,
    ListAllEmpleadosView,
    ListByAreaEmpleadosView,
    BuscarEmpleadoByKwordView,
    EmpleadoDetailView,
    EmpleadoCreateView,
    SuccessView,
    EmpleadoUpdateView,
    SuccessUpdateView,
    EmpleadoDeleteView,
    SuccessDeleteUpdateView
    )

app_name = 'persona'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list-all-empleados/', ListAllEmpleadosView.as_view(), name='list-all'),
    path('list-by-area/<name>/', ListByAreaEmpleadosView.as_view(), name='list-by-area'),
    path('buscar-empleado/', BuscarEmpleadoByKwordView.as_view(), name='buscar-empleado'),
    path('detail-empleado/<pk>/', EmpleadoDetailView.as_view(), name='detail-empleado'),
    path('add-empleado/', EmpleadoCreateView.as_view(), name='add-empleado'),
    path('success/', SuccessView.as_view(), name='success'),
    path('update-empleado/<pk>/', EmpleadoUpdateView.as_view(), name='update-empleado'),
    path('update-success/', SuccessUpdateView.as_view(), name='update-success'),
    path('delete-empleado/<pk>/', EmpleadoDeleteView.as_view(), name='empleado-delete'),
    path('delete-success/', SuccessDeleteUpdateView.as_view(), name='empleado-delete-success'),
]
