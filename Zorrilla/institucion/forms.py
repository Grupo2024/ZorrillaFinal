from django import forms
from .models import clave_Docente

class clave_DocenteForm(forms.ModelForm):
    class Meta:
        model = clave_Docente
        fields = ('email_docente','dni_docente',)
        