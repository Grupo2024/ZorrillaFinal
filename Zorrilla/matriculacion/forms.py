# -*- coding: utf-8 -*-
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

class RelacionForm(forms.Form):
    relacion_con_alumno = forms.CharField(required=True)

class ReMatricularForm(forms.Form):
    dni_alumno = forms.IntegerField(required=True)
    dni_padre = forms.IntegerField(required=True)
    email_padre = forms.EmailField(required=True)

class AutorizadoForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(error_messages={'invalid':"Fecha no valida: '2000-10-31'"})
    class Meta:
        model = Autorizado
        fields = '__all__'
        
class EditarAutorizadoForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(error_messages={'invalid':"Fecha no valida: '31-5-2000'"})
    class Meta:
        model = Autorizado
        fields = ['nombre', 'apellido','lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','telefono_autorizado']

class SDForm(forms.Form):
    class Meta:
        model = Trabajador
        fields =('nombre_t','apellido_t','dni_t','fecha_nacimiento_t','lugar_nacimiento_t','domicilio_t','email_t','sexo_t','telefono_particular','telefono_laboral',
 'telefono_familiar','datos_familiares_cargo','antecedentes_laborales','estudios_cursados')
        widgets = {
            'fecha_nacimiento_t': DateInput()
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

class EditarPadreForm(forms.ModelForm):
    class Meta:
        model = Padre_madre
        fields = ['nombre', 'apellido','lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','profesion','telefono_trabajo']

class EditarIndexForm(forms.ModelForm):
    class Meta:
        model = datos_Index
        fields = '__all__'

class EditarTransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        fields = ['nombre', 'apellido', 'lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','nombre_transporte',
'telefono_transportista','detalles_transportista']
        widgets = {
          'detalles_transportista': forms.Textarea(attrs={'rows':3, 'cols':20}),
        }


class TransportistaForm(forms.ModelForm):
    class Meta:
        model = Transportista
        fields =  ['nombre', 'apellido', 'dni', 'lugar_nacimiento','fecha_nacimiento','domicilio','email','sexo','nombre_transporte',
'telefono_transportista','detalles_transportista']
        widgets = {
            'detalles_transportista': forms.Textarea(attrs={'rows':3, 'cols':20}),
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

    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    lugar_nacimiento = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(required=True)
    domicilio = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    sexo = forms.ChoiceField(choices=GENERO_CHOICES)
    telefono_casa = forms.IntegerField(required=True)
    telefono_padre = forms.IntegerField(required=True)
    telefono_madre = forms.IntegerField(required=True)
    telefono_familiar = forms.IntegerField(required=True)
    telefono_vecino = forms.IntegerField(required=True)
    enfermedad_relevante = forms.CharField(required=True)
    con_quien_vive = forms.CharField(required=True)
    quien_lo_trae = forms.CharField(required=True)
    telefono_que_lo_trae = forms.IntegerField(required=True)
