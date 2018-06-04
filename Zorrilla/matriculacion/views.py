# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import *
from .creation import *
from .test_model import *
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')

def solicitar_matriculacion(request):
    print request.user
    alumnos = Alumno.objects.all()
    print alumnos
    matriculaciones = Matriculacion.objects.filter(matriculado=False)
    print matriculaciones
    return render(request, 'pedidos.html', {'matriculaciones':matriculaciones})

def aceptar_matriculacion(request, id_matriculacion):
    print "eentra"
    matriculacion = Matriculacion.objects.get(id=id_matriculacion)
    matriculacion.matriculado = True
    matriculacion.save()
    if matriculacion_estado(id_matriculacion):
        data = {
            'estado': "El alumno " + str(matriculacion.alumno.apellido) + " " + str(matriculacion.alumno.nombre) + " esta matriculado"
        }
    else:
        fallo_matriculando(id_matriculacion)
        data = {
            'estado':"La matriculacion falló"
        }
    return JsonResponse(data, safe=False)
