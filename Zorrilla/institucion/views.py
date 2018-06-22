# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from matriculacion.models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

def cursos1(request):
    return render(request, 'templates_cursos/cursos1.html')

def cursos2(request):
    return render(request, 'templates_cursos/cursos2.html')

def cursos3(request):
    return render(request, 'templates_cursos/cursos3.html')

def cursos4(request):
    return render(request, 'templates_cursos/cursos4.html')

def docentes(request):
    profesores = Profesor.objects.all()
    return render(request, 'templates_docentes/docentes.html', {'profesores':profesores})


def profesor(request, id_profesor):
    profesor = Profesor.objects.get(dni=id_profesor)
    profesor.sexo = profesor.genero()
    return render(request, 'templates_docentes/perfilProfesor.html', {'profesor':profesor})

def eliminar_docente(request, id_profesor):
    profesor = Profesor.objects.get(dni=id_profesor)
    if profesor.delete():
        data = {
            'resultado': "El profesor fue eliminado"
        }
    else:
        data = {
            'resultado': "Hubo un error"
        }
    return JsonResponse(data, safe=True)


