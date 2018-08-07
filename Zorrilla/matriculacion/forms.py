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
        fields =('nombre','apellido','dni','lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','telefono_casa','telefono_padre',
 'telefono_madre','telefono_familiar','telefono_vecino','enfermedad_relevante','con_quien_vive','telefono_que_lo_trae','utiliza_transporte','tiene_obra_social','obra_social_nombre','obra_social_numero')
        widgets = {
            'fecha_nacimiento': DateInput()
        }
        
class get_Password(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()