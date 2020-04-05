from django.contrib import admin
from .models import Empleado, Habilidad

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'departamento', 'job']
    search_fields = ['first_name', 'last_name', 'departamento__name']
    list_filter = ['departamento', 'job', 'habilidad']
    filter_horizontal = ['habilidad']

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidad)
