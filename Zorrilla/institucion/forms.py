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
