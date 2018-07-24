# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import *
from .creation import *
from .test_model import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.

def asdf(request):
    alumno = AlumnoForm
    return render(request, 'test.html', {'form':alumno})

def index(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')

def cursos(request):
    return render(request, 'cursos.html')

def logIn(request):
    return render(request, 'docentes_login.html')

def logout_me_out(request):
    auth.logout(request)
    return redirect ('index')

def get_Secciones(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    seccion = Seccion.objects.filter('grado_asignado.aNo','curso')
    return render(request, 'select_curso.html', {'secciones':seccion, 'alumno':alumno})

def aceptar_matriculaciones(request):
    alumnos = Alumno.objects.all()
    matriculaciones = Matriculacion.objects.filter(matriculado=False)
    return render(request, 'pedidos.html', {'matriculaciones':matriculaciones})

def aceptar_matriculacion(request):
    if request.method == 'POST':
        dni_alumno = request.POST['dni_alumno']
        print dni_alumno
        selected_curso = request.POST['selected_curso']
        print selected_curso
        seccion = Seccion.objects.get(id=selected_curso)
        alumno = Alumno.objects.get(dni=dni_alumno)
        matriculacion = Matriculacion.objects.get(alumno=alumno)
        matriculacion.matriculado = True
        matriculacion.save()
        alumno.seccion_asignada = seccion
        alumno.save()
        if alumno.seccion_asignada is not None:
            data = {
                'estado': "El alumno " + str(alumno.apellido) + "" + str(alumno.nombre) + " asiste al curso " + str(alumno.seccion_asignada),
                'error': False
            }
        else:
            data = {
                'estado':'Hubo un error',
                'error': True
            }
    return JsonResponse(data, safe=True)

def alumno(request, id_alumno):
    alumno = Alumno.objects.get(dni=id_alumno)
    alumno.sexo = alumno.genero()
    return render(request, 'perfilAlumno.html', {'alumno':alumno})

def login(request):
    if request.method == 'POST':
        print "llegea el login"
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            data = {
                'error': False
            }
        else:           
            data = {
            'estado': "nombre de usuario o contraseña no son correctos",
            'error': True
            }
    return JsonResponse(data, safe=True)
