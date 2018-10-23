from django.db import models
from .models import *
import random

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


def new_Password(dni):
    try:
        profesor = Profesor.objects.get(dni_t=dni)
        nombre = profesor.nombre_t
        apellido = profesor.apellido_t
    except Profesor.DoesNotExist:
        nombre = ""
        apellido = ""
    try:
        director = Director.objects.get(dni_t=dni)
        nombre = director.nombre_t
        apellido = director.apellido_t
    except Director.DoesNotExist:
        nombre = ""
        apellido = ""
    name_f = ""
    cantidad = 0
    r = random.randint(1111,9999)
    for a in nombre:
        cantidad = cantidad + 1
        if cantidad == 1:
            name_f = a
            break
        else:
            pass
    password = name_f + apellido + str(r)
    return password
