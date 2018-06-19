# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import *
from .creation import *
from .test_model import *
from django.http import JsonResponse
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')

def cursos(request):
    return render(request, 'cursos.html')

def logIn(request):
    return render(request, 'docentes_login.html')

def logout_me_out(request):
    print "logueate gato"
    auth.logout(request)
    return redirect ('index')

def aceptar_matriculaciones(request):
    alumnos = Alumno.objects.all()
    matriculaciones = Matriculacion.objects.filter(matriculado=False)
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

def alumno(request, id_alumno):
    alumno = Alumno.objects.get(dni=id_alumno)
    alumno.sexo = alumno.genero()
    return render(request, 'perfilAlumno.html', {'alumno':alumno})
