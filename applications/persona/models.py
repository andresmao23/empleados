from django.db import models
from applications.departamento.models import Departamento

class Habilidad(models.Model):
    name = models.CharField('Nombre', max_length=20, unique=True)

    def __str__(self):
        return self.name

class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Ingeniero'),
        ('2', 'Economista')
    )

    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidad = models.ManyToManyField(Habilidad)
    #image = models.ImageField(upload_to='persona', blank=True, null=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name