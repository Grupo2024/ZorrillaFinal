# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from matriculacion.models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .crear_docente import *
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import *
import random

def email_for_logIn(request):
    if request.method == 'POST':
        form = clave_DocenteForm(request.POST)
        if form.is_valid():
            docente_email = form.cleaned_data['email_docente']
            docente_dni = form.cleaned_data['dni_docente']
            clave = request.POST['claveDoc']
            profesor = Profesor.objects.get(email_t=docente_email)
            ingresado = False
            clave_Docente2 = clave_Docente(clave_logIn=clave, email_docente=docente_email, dni_docente=docente_dni, ingresado=ingresado)
            clave_Docente2.save()
            subject = "Cambio de clave"
            message = "En el dia de la fecha el instituto Zorrilla le notifica que al usuario con direccion" + str(profesor.email_t) + " de dni: " + str(profesor.dni_t) + " se le ha cambiado la contraseña a " + str(clave)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [docente_email]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('template_email_docente')
    else:
        print "no funca"
    return render(request, 'templates_docentes/emailDocente.html')

def template_email_docente(request):
    
    ran = random.randrange(10**80)
    myhex = "%064x" % ran
    clave = myhex[:10].upper()
    dic = {
        'clave':clave
    }
    form = clave_DocenteForm()
    return render(request, 'templates_docentes/emailDocente.html', {'form':form, 'clave':dic})

def cursos1(request):
    return render(request, 'templates_cursos/cursos1.html')

def cursos2(request, turno):
    print turno
    if turno == "Maniana":
        turno = False
    else:
        turno = True
    curso = Curso.objects.filter(hora=turno).order_by('aNo')
    for a in curso:
        a.new_turno()
    return render(request, 'templates_cursos/cursos2.html', {'todos_los_cursos':curso}, {'turno':turno} )

def cursos3(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    alumno = Alumno.objects.filter(curso=curso)
    data_curso = {
        'turno':curso.que_turno(),
        'año':curso.aNo,
        'seccion':curso.que_seccion()
    }
    return render(request, 'templates_cursos/cursos3.html', {'todos_los_alumnos':alumno, 'curso':data_curso})

def get_alumno(request, string, dni_alumno):
    if request.method == 'POST':
        alumno = Alumno.objects.get(dni=dni_alumno)
        alumno.genero = alumno.genero()
        if string == "telefonos":
            print "telefono"
            return render(request, 'templates_cursos/telefonos_alumno.html', {'alumno':alumno})
        else:
            print "otro"
            return render(request, 'templates_cursos/perfil_alumno.html', {'alumno':alumno})
    return HttpResponse("SOlo podes entrar por post")

def datos_alumno(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    alumno.sexo = alumno.genero()
    return render(request, 'perfilAlumno.html', {'alumno':alumno})

def docentes(request):
    profesores = Profesor.objects.all()
    for a in profesores:
        a.genero = a.genero()
        print a.nombre_t
    return render(request, 'templates_docentes/docentes.html', {'profesores':profesores})


def profesor(request, id_profesor):
    profesor = Profesor.objects.get(dni_t=id_profesor)
    profesor.sexo = profesor.genero()
    return render(request, 'templates_docentes/perfilProfesor.html', {'trabajador':profesor})

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

def formProfesor(request):
    return render(request, 'templates_docentes/formProfesor.html')
