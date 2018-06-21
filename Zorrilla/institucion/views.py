# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from matriculacion.models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import *

def cursos1(request):
    return render(request, 'templates_cursos/cursos1.html')

"""
def cursos2(request, turno):
    if turno == 'Maniana':
        turno = False
    else:
        turno = True
    grados = Grado.objects.filter(turno_asignado__hora = turno)
    for grado in grados:
        if turno:
            grado.turno = "Tarde"
        else:
            grado.turno = "Maniana"
    return render(request, 'templates_cursos/cursos2.html', {'todos_los_grados':grados})

"""

def cursos2(request, turno):
    print turno
    if turno == "Maniana":
        turno = False
    else:
        turno = True
    grados = Grado.objects.filter(turno_asignado__hora=turno)
    return render(request, 'templates_cursos/cursos2.html', {'todos_los_grados':grados})

def cursos3(request, id_grado):
    grado = Grado.objects.get(pk=id_grado)
    seccion = Seccion.objects.filter(grado_asignado = grado)
    return render(request, 'templates_cursos/cursos3.html', {'secciones_de_grados':seccion})



def cursos4(request):
    return render(request, 'templates_cursos/cursos4.html')

def docentes(request):
    profesores = Profesor.objects.all()
    return render(request, 'templates_docentes/docentes.html', {'profesores':profesores})


def profesor(request, id_profesor):
    profesor = Profesor.objects.get(dni=id_profesor)
    profesor.sexo = profesor.genero()
    return render(request, 'templates_docentes/perfilProfesor.html', {'profesor':profesor})


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:           
            return HttpResponse("No Existe ese User")
    return HttpResponse("Tenes que entrar por Post")
