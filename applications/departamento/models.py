from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return self.name
