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
        model = Profesor
        fields =('nombre_t','apellido_t','dni_t','fecha_nacimiento_t','lugar_nacimiento_t','domicilio_t','email_t','sexo_t','telefono_particular','telefono_laboral',
 'telefono_familiar','datos_familiares_cargo','antecedentes_laborales','estudios_cursados')
        widgets = {
            'fecha_nacimiento_t': DateInput()
        }

class ModificarForm(forms.Form):

    HO = 'Hombre'
    MU = 'Mujer'

    GENERO_CHOICES = (
        (HO , 'Hombre'),
        (MU , 'Mujer'),
    )

    nombre = forms.CharField(required=True)
    apellido =forms.CharField(required=True)
    lugar_nacimiento = forms.CharField(required=True)
    fecha_nacimiento = forms.DateField(required=True)
    domicilio = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    sexo = forms.ChoiceField(choices=GENERO_CHOICES, required=True)
    telefono_particular = forms.IntegerField(required=True)
    telefono_laboral = forms.IntegerField(required=True)
    telefono_familiar = forms.IntegerField(required=True)
    datos_familiares_cargo = forms.CharField(required=True, widget=forms.Textarea)
    fecha_inicio_actividad = forms.DateField(required=True)
    antecedentes_laborales = forms.CharField(required=True, widget=forms.Textarea)
    estudios_cursados = forms.CharField(required=True, widget=forms.Textarea)
