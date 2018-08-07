# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from .creation import *
from .test_model import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def asdf(request):
    alumno = AlumnoForm
    return render(request, 'test.html', {'form':alumno})

def index(request):
    print "index"
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
    print "enrea"
    if request.method == 'POST':
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


#Function that render my_info Template wuth a form to get my new password.
def template_get_pass(request):
    form = get_Password()
    return render (request, 'new_password/my_info.html', {'form':form})

def userDocente(request):
    if request.method == "POST":
        form = get_Password(request.POST)
        if form.is_valid():
            print "es valido"
            email = form.cleaned_data['email']
            apellido = form.cleaned_data['apellido']
            nombre = form.cleaned_data['nombre']
            dni = form.cleaned_data['dni']
            errores = docente_existe(email, apellido, nombre, dni)
            if len(errores) != 0:
                error = ""
                espacio = "-"
                for a in errores:
                    error = error + espacio + a
                data = {
                    'resultado': error
                }
                return JsonResponse(data)
            else:
                print "no hay errores"
                profesor = Profesor.objects.get(dni_t=dni)
                userD = user_Docente.objects.get(docente_referenciado=profesor)
                print userD.user.username
                new_pass = new_Password(profesor.dni_t)
                subject = "Recuperar Contraseña"
                message = "El usuario " + str(userD.user.username) + " utilizara la siguiente contraseña " + str(new_pass)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [profesor.email_t]
                if send_mail( subject, message, email_from, recipient_list):
                    data = {
                        'usuario': userD.user.username,
                        'email': profesor.email_t
                    }
                print "funciona"
                userd = User.objects.get(username=userD.user.username)
                userd.password = new_pass
                userd.save()
                return render (request, 'new_password/done.html', {'info':data})
                
        else:
            return HttpResponse("Esta mal xd")
