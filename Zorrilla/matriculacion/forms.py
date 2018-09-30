from django import forms
from .models import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import extras
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields =['nombre','apellido','dni','lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','telefono_casa','telefono_padre'
,'telefono_madre','telefono_familiar','telefono_vecino','enfermedad_relevante','con_quien_vive','quien_lo_trae','telefono_que_lo_trae']
        widgets = {
            'fecha_nacimiento': DateInput()
        }

class PadreForm(forms.ModelForm):
    class Meta:
        model = Padre_madre
        fields = ['nombre', 'apellido', 'dni', 'lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','profesion','telefono_trabajo']
        widgets = {
            'fecha_nacimiento': DateInput()
        }

class get_Password(forms.Form):
    dni = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
