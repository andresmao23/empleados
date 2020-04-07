from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('__all__')
        labels = {
            'first_name': ('Nombres'),
        }
        help_texts = {
            'first_name': ('Nombre o nombres del empleado'),
            'habilidad': ('Use la combinación (Ctr + clic) para seleccionar varias opciones.'),
        }
        error_messages = {
            'first_name': {
                'max_length': ("El nombre del empleado supera la longitud máxima (50 caracteres.)"),
            },
            'last_name': {
                'max_length': ("El apellido del empleado supera la longitud máxima (50 caracteres.)"),
            },
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese texto aquí.',
                    #'class': 'special',
                    #'size': '40'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese texto aquí.'
                }
            )
        }