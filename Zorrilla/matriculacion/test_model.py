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
    docente = Profesor.objects.filter(dni_t=dni)
    if docente:
        pass
    else:
        incoherencias.append("Dni")
    docente = Profesor.objects.filter(nombre_t=nombre)
    if docente:
        pass
    else:
        incoherencias.append(" Nombre")
    docente = Profesor.objects.filter(apellido_t=apellido)
    if docente:
        pass
    else:
        incoherencias.append(" Apellido")
    docente = Profesor.objects.filter(email_t=email)
    if docente:
        pass
    else:
        incoherencias.append(" Email")
    return incoherencias

def new_Password(dni):
    docente = Profesor.objects.get(dni_t=dni)
    name_f = ""
    cantidad = 0
    r = random.randint(1111,9999)
    for a in docente.nombre_t:
        cantidad = cantidad + 1
        if cantidad == 1:
            name_f = a
            break
        else:
            pass
    password = name_f + docente.apellido_t + str(r)
    return password
