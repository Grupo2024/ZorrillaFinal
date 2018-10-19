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


class Obra_SocialForm(forms.ModelForm):
    class Meta:
        model= Obra_Social
        fields = ['nombre']

class PadreForm(forms.ModelForm):
    class Meta:
        model = Padre_madre
        fields = ['nombre', 'apellido', 'dni', 'lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','profesion','telefono_trabajo']
        widgets = {
            'fecha_nacimiento': DateInput()
        }

class TransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        fields =  ['nombre', 'apellido', 'dni', 'lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','nombre_transporte',
'telefono_transportista','detalles_transportista']
        widgets = {
            'fecha_nacimiento': DateInput()
        }

class get_Password(forms.Form):
    dni = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)


class Modificar_Alumno_Form(forms.Form):

    HO = 'Hombre'
    MU = 'Mujer'

    GENERO_CHOICES = (
        (HO , 'Hombre'),
        (MU , 'Mujer'),
    )

    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    lugar_nacimiento = forms.CharField(required=False)
    fecha_nacimiento = forms.DateField(required=False)
    domicilio = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    sexo = forms.ChoiceField(choices=GENERO_CHOICES)
    telefono_casa = forms.IntegerField(required=False)
    telefono_padre = forms.IntegerField(required=False)
    telefono_madre = forms.IntegerField(required=False)
    telefono_familiar = forms.IntegerField(required=False)
    telefono_vecino = forms.IntegerField(required=False)
    enfermedad_relevante = forms.CharField(required=False)
    con_quien_vive = forms.CharField(required=False)
    quien_lo_trae = forms.CharField(required=False)
    telefono_que_lo_trae = forms.IntegerField(required=False)
