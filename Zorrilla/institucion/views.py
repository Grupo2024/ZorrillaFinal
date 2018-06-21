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


def dmain(request):
    return render(request, 'templates_directora/directora_main.html')