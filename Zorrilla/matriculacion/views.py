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
from biblioteca.decorators import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def formulario(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = AlumnoForm()
            return render(request, 'formulario.html', {'form':form})

    else:
        form = AlumnoForm()
    return render(request, 'formulario.html', {'form':form})

def logIn(request):
    return render(request, 'docentes_login.html')

@login_required
def logout_me_out(request):
    auth.logout(request)
    return redirect ('index')

#Esta hay que corregirla
def get_Secciones(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    seccion = Seccion.objects.filter('grado_asignado.aNo','curso')
    return render(request, 'select_curso.html', {'secciones':seccion, 'alumno':alumno})

@user_passes_test(check_Secretaria)
def aceptar_matriculaciones(request):
    matriculaciones = Matriculacion.objects.filter(matriculado=False)
    if matriculaciones:
        return render(request, 'pedidos.html', {'matriculaciones':matriculaciones})
    else:
        matriculaciones = []
        return render(request, 'pedidos.html', {'matriculaciones':matriculaciones})

#Hay que arreglarlo
@user_passes_test(check_Secretaria)
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

@login_required
def alumno(request, id_alumno):
    alumno = Alumno.objects.get(dni=id_alumno)
    alumno.sexo = alumno.genero()
    return render(request, 'perfilAlumno.html', {'alumno':alumno})

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        print username
        print password
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


#Function that render my_info Template with a form to get my new password.
def template_get_pass(request):
    form = get_Password()
    return render (request, 'new_password/my_info.html', {'form':form})

#Funcion para cambiar la password del usuario.
def userDocente(request):
    if request.method == "POST":
        form = get_Password(request.POST)
        if form.is_valid():
            print "es valido"
            email = form.cleaned_data['email']
            dni = form.cleaned_data['dni']
            try:
                profesor = Profesor.objects.get(email_t=email)
                try:
                    profesor = Profesor.objects.get(dni_t=dni)
                    userD = user_Docente.objects.get(docente_referenciado=profesor)
                    print userD.user.username
                    new_pass = new_Password(profesor.dni_t)
                    subject = "Recuperar Contraseña"
                    message = "El usuario " + str(userD.user.username) + " utilizara la siguiente contraseña " + str(new_pass)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [profesor.email_t]
                    send_mail( subject, message, email_from, recipient_list)
                    print "funciona"
                    userd = User.objects.get(username=userD.user.username)
                    print "Vieja Pass" + str(userd.password)
                    userd.set_password(new_pass)
                    userd.save()
                    print "nueva pass" + str(userd.password)
                    data = {
                        'email': email,
                        'dni': dni,
                        'resultado': "Clave cambiada con exito.",
                        'error':False
                    }
                    return JsonResponse(data)
                except Profesor.DoesNotExist:
                    data = {
                        'email': email,
                        'dni': "No existe un profesor con ese Dni.",
                        'resultado': "Hubo un error",
                        'error':True
                    }
                    return JsonResponse(data)
            except Profesor.DoesNotExist:
                data = {
                    'email': "No existe un profesor con esta direccion",
                    'dni': "-",
                    'resultado': "Hubo un error",
                    'error':True
                }
                return JsonResponse(data)
        else:
            print "NO ES VALIDO"
            data = {
                'email': "-",
                'dni': "-",
                'resultado': "Error de validez",
                'error':True
            }
            return JsonResponse(data)
