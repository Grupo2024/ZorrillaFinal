from django import forms
from .models import clave_Docente, Profesor

class clave_DocenteForm(forms.ModelForm):
    class Meta:
        model = clave_Docente
        fields = ('email_docente','dni_docente',)


class form_Profesor(forms.ModelForm):
	class Meta:
		model = Profesor
		fields = "__all__"


        