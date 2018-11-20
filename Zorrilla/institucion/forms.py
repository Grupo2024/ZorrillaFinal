from django import forms
from .models import *

class clave_DocenteForm(forms.ModelForm):
    class Meta:
        model = clave_Docente
        fields = ('email_docente','dni_docente',)

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields =('nombre_t','apellido_t','dni_t','fecha_nacimiento_t','lugar_nacimiento_t','domicilio_t','email_t','sexo_t','telefono_particular','telefono_laboral',
 'telefono_familiar','datos_familiares_cargo','antecedentes_laborales','estudios_cursados')
        widgets = {
            'fecha_nacimiento_t': DateInput()
        }

class Modificar_Trabajador_Form(forms.Form):
    HO = 'Hombre'
    MU = 'Mujer'

    GENERO_CHOICES = (
        (HO , 'Hombre'),
        (MU , 'Mujer'),
    )

    nombre_t = forms.CharField(required=True)
    apellido_t =forms.CharField(required=True)
    fecha_nacimiento_t = forms.DateField(required=True)
    lugar_nacimiento_t = forms.CharField(required=True)
    domicilio_t = forms.CharField(required=True)
    email_t = forms.EmailField(required=True)
    sexo_t = forms.ChoiceField(choices=GENERO_CHOICES, required=True)
    telefono_particular = forms.IntegerField(required=True)
    telefono_laboral = forms.IntegerField(required=True)
    telefono_familiar = forms.IntegerField(required=True)
    datos_familiares_cargo = forms.CharField(required=True, widget=forms.Textarea)
    antecedentes_laborales = forms.CharField(required=True, widget=forms.Textarea)
    estudios_cursados = forms.CharField(required=True, widget=forms.Textarea)
