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
            ingresado = False
            clave_Docente2 = clave_Docente(clave_logIn=clave, email_docente=docente_email, dni_docente=docente_dni, ingresado=ingresado)
            clave_Docente2.save()
            subject = "Su hijo es un auto"
            message = "En el dia de la fecha el instituto Zorrilla le notifica que " + str(docente_email) + str(docente_dni) + str(clave)
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
    return render(request, 'templates_cursos/cursos2.html', {'todos_los_grados':grados}, {'turno':turno} )

def cursos3(request, id_grado):
    grado = Grado.objects.get(pk=id_grado)
    seccion = Seccion.objects.filter(grado_asignado = grado)
    return render(request, 'templates_cursos/cursos3.html', {'secciones_de_grados':seccion})

def cursos4(request, id_seccion):
    seccion = Seccion.objects.get(id=id_seccion)
    alumnos = Alumno.objects.filter(seccion_asignada=seccion)
    return render(request, 'templates_cursos/cursos4.html',{'alumnos':alumnos})

def docentes(request):
    profesores = Profesor.objects.all()
    for a in profesores:
        a.genero = a.genero()
        print a.nombre_t
    return render(request, 'templates_docentes/docentes.html', {'profesores':profesores})


def profesor(request, id_profesor):
    profesor = Profesor.objects.get(dni_t=id_profesor)
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

def formProfesor(request):
    return render(request, 'templates_docentes/formProfesor.html')
