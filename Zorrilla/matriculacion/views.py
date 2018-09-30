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

def daddy():
    cant_profesores = Profesor.objects.all().count()
    if cant_profesores == 0:
        password = "hola1234"
        user_secretaria = User.objects.create_user(username="secretaria", password=password)
        grupo_secretaria, created = Group.objects.get_or_create(name='Secretaria')
        user_profesor = User.objects.create_user(username="profesor", password=password)
        grupo_profesor, created = Group.objects.get_or_create(name='Profesor')
        user_director = User.objects.create_user(username="director", password=password)
        grupo_director, created = Group.objects.get_or_create(name='Director')
        grupo_secretaria = Group.objects.get(name='Secretaria') 
        grupo_secretaria.user_set.add(user_secretaria)
        my_group2 = Group.objects.get(name='Profesor') 
        my_group2.user_set.add(user_profesor)
        my_group3 = Group.objects.get(name='Director') 
        my_group3.user_set.add(user_director)
        #new_group, created = Group.objects.get_or_create(name='new_group')
        a = Secretaria(nombre_t="a", apellido_t="a", dni_t=11111111, lugar_nacimiento_t="a", 
        fecha_nacimiento_t="1980-01-01", domicilio_t="a", email_t="mumi@gmail.com", sexo_t="Mujer", 
        telefono_particular=1, telefono_laboral=1, telefono_familiar=1, datos_familiares_cargo="a",
        fecha_inicio_actividad="2018-03-01", antecedentes_laborales="a", estudios_cursados="a") 
        b = Profesor(nombre_t="b", apellido_t="b", dni_t=22222222, lugar_nacimiento_t="b", 
        fecha_nacimiento_t="1980-02-02", domicilio_t="b", email_t="pancho@gmail.com", sexo_t="Hombre", 
        telefono_particular=2, telefono_laboral=2, telefono_familiar=2, datos_familiares_cargo="b",
        fecha_inicio_actividad="2018-02-02", antecedentes_laborales="b", estudios_cursados="b")
        c = Director(nombre_t="c", apellido_t="c", dni_t=33333333, lugar_nacimiento_t="c", 
        fecha_nacimiento_t="1980-03-03", domicilio_t="c", email_t="arce@gmail.com", sexo_t="dudoso", 
        telefono_particular=3, telefono_laboral=3, telefono_familiar=3, datos_familiares_cargo="c",
        fecha_inicio_actividad="2018-03-03", antecedentes_laborales="c", estudios_cursados="c")
        a.save()
        b.save()
        c.save()
        secretaria_aux = user_Secretaria(user=user_secretaria,secretaria_referenciada=a)
        profesor_aux = user_Docente(user=user_profesor,docente_referenciado=b)
        director_aux = user_Director(user=user_director,director_referenciado=c)
        secretaria_aux.save()
        profesor_aux.save()
        director_aux.save()
        return "Creados"
    else:
        return "Ya estan creados"

def index(request):
    daddy()
    return render(request, 'index.html')

def formulario(request):
    alumno_form = AlumnoForm()
    padre_form = PadreForm()
    return render(request, 'formulario.html', {'alumno_form':alumno_form, 'padre_form':padre_form})

def crear_alumno(request):
    alumno_form = AlumnoForm(request.POST)
    if alumno_form.is_valid():
        alumno_form.save()
        dni_alumno = alumno_form.cleaned_data['dni']
        apellido_alumno = alumno_form.cleaned_data['apellido']
        nombre_alumno = alumno_form.cleaned_data['nombre']
        alumno = Alumno.objects.get(dni=dni_alumno)
        datos_alumno = {
            'dni_alumno':dni_alumno,
            'apellido_alumno':apellido_alumno,
            'nombre_alumno':nombre_alumno
        }
        padre_form = PadreForm()
        return render(request, 'cargar_padre.html', {'padre_form':padre_form, 'datos_alumno':datos_alumno})
    else:
        aux = alumno_form.errors
        return HttpResponse(str(aux))

def crear_padre(request):
    padre_form = PadreForm(request.POST)
    dni_alumno = request.POST['dni_alumno']
    alumno = Alumno.objects.get(dni=dni_alumno)
    if padre_form.is_valid():
        padre_form.save()
        dni_padre = padre_form.cleaned_data['dni']
        padre = Padre_madre.objects.get(dni=dni_padre)
        print padre
        familia = Familia(alumno=alumno, padre_madre=padre)
        familia.save()
        new_Matriculacion = Matriculacion(alumno=alumno)
        new_Matriculacion.save()
        resultado = "Los pedidos de Matriculacion de " + str(padre.apellido) + "" + str(padre.nombre) + " y de " + str(alumno.apellido) + "" + str(alumno.nombre) + " han sido creados con exito"
        data = {
            'error':False,
            'resultado':resultado
        }
        return JsonResponse(data)
    else:
        resultado = str(padre_form.errors)
        data = {
            'error':True,
            'resultado':resultado
        }
        return JsonResponse(data)

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
        print (dni_alumno)
        selected_curso = request.POST['selected_curso']
        print (selected_curso)
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
        print (username)
        print (password)
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
            print ("es valido")
            email = form.cleaned_data['email']
            dni = form.cleaned_data['dni']
            try:
                profesor = Profesor.objects.get(email_t=email)
                try:
                    profesor = Profesor.objects.get(dni_t=dni)
                    userD = user_Docente.objects.get(docente_referenciado=profesor)
                    print (userD.user.username)
                    new_pass = new_Password(profesor.dni_t)
                    subject = "Recuperar Contraseña"
                    message = "El usuario " + str(userD.user.username) + " utilizara la siguiente contraseña " + str(new_pass)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [profesor.email_t]
                    #send_mail( subject, message, email_from, recipient_list)
                    print ("funciona")
                    userd = User.objects.get(username=userD.user.username)
                    print ("Vieja Pass" + str(userd.password))
                    #userd.set_password(new_pass)
                    #userd.save()
                    print ("nueva pass" + str(userd.password))
                    data = {
                        'resultado': "Clave cambiada con exito.",
                        'error':False
                    }
                    return JsonResponse(data)
                except Profesor.DoesNotExist:
                    data = {
                        'resultado': "No existe un profesor con esta direccion de Email.",
                        'error':True
                    }
                    return JsonResponse(data)
            except Profesor.DoesNotExist:
                    data = {
                        'resultado': "No existe un profesor con ese Dni.",
                        'error':True
                    }
                    return JsonResponse(data)
        else:
            print (form.errors)
            aux = form.errors
            data = {
                'resultado': str(form.errors),
                'error':True
            }
            return JsonResponse(data)
