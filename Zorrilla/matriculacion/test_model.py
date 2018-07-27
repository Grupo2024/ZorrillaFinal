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

def docente_existe(email, apellido, nombre, dni):
    incoherencias = []
    if docente == Docente.objects.get(dni=dni):
        pass
    else:
        incoherencias.append("Dni")
    if docente == Docente.objects.get(nombre=nombre):
        pass
    else:
        incoherencias.append(" Nombre")
    if docente == Docente.objects.get(apellido=apellido):
        pass
    else:
        incoherencias.append(" Apellido")
    if docente == Docente.objects.get(email=email):
        pass
    else:
        incoherencias.append(" Email")
    return incoherencias

def new_Password(dni):
    docente = Docente.objects.get(dni=dni)
    name_f = ""
    cantidad = 0
    r = random.randint(1111,9999)
    for a in docente.nombre:
        cantidad = cantidad + 1
        if cantidad == 1:
            name_f = a
            break
        else:
            pass
    password = name_f + docente.apellido + r
    return password
    