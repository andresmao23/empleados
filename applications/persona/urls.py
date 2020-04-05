from django.urls import path
from .views import IndexView, ListAllEmpleadosView

app_name = 'persona'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list-all-empleados/', ListAllEmpleadosView.as_view(), name='list-all')
]
