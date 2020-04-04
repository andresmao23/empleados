from django.urls import path

def saludar(self):
    print('****************** Hola mundo desde la función saludar desde la app Departamento ******************')

urlpatterns = [
    path('saludardepartamento/', saludar),
]
