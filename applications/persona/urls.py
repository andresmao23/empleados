from django.urls import path
from .views import IndexView, ListAllEmpleadosView, ListByAreaEmpleadosView

app_name = 'persona'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list-all-empleados/', ListAllEmpleadosView.as_view(), name='list-all'),
    path('list-by-area/<name>/', ListByAreaEmpleadosView.as_view(), name='list-by-area')
]
