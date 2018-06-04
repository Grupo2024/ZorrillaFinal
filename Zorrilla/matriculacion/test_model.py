from django.db import models
from .models import *

def matriculacion_estado(id_matriculacion):
    matriculacion = Matriculacion.objects.get(id=id_matriculacion)
    if matriculacion.matriculado:
        return True
    else:
        return False

def fallo_matriculando(id_matriculacion):
    if matriculacion_estado(id_matriculacion):
        matriculacion = Matriculacion.objects.get(id=id_matriculacion)
        matriculacion.matriculado = False
        matriculacion.save()
    else:
        pass
