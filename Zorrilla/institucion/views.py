# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from matriculacion.models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import *
from biblioteca.decorators import *
from .crear_docente import *
import random
import datetime

@user_passes_test(check_Secretaria)
def email_for_logIn(request):
    if request.method == 'POST':
        form = clave_DocenteForm(request.POST)
        if form.is_valid():
            docente_email = form.cleaned_data['email_docente']
            docente_dni = form.cleaned_data['dni_docente']
            clave = request.POST['claveDoc']
            clave_Docente2 = clave_Docente(clave_logIn=clave, email_docente=docente_email, dni_docente=docente_dni)
            clave_Docente2.save()
            subject = "Clave para Iniciar"
            message = "En el dia de la fecha el Instituto Zorrilla le notifica que ya tiene disponible el ingreso al formulario para cargar sus datos en nuestro sistema con la clave " + str(clave)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [docente_email]
            send_mail( subject, message, email_from, recipient_list )
            data = {
                'error':False,
                'resultado': "Pedido enviado"
            }
            print "es valido"
            return JsonResponse(data)
        else:
            print "No es valido"
            print form.errors
            data = {
                'error':True,
                'resultado': "No es valido"
            }
            return JsonResponse(data)

@user_passes_test(check_Secretaria)
def template_email_docente(request):
    ran = random.randrange(10**80)
    myhex = "%064x" % ran
    clave = myhex[:10].upper()
    dic = {
        'clave':clave
    }
    form = clave_DocenteForm()
    return render(request, 'templates_docentes/emailDocente.html', {'form':form, 'clave':dic})

@login_required
def cursos1(request):
    return render(request, 'templates_cursos/cursos1.html')

@login_required
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

@login_required
def cursos3(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    alumno = Alumno.objects.filter(curso=curso)
    data_curso = {
        'turno':curso.que_turno(),
        'año':curso.aNo,
        'seccion':curso.que_seccion()
    }
    return render(request, 'templates_cursos/cursos3.html', {'todos_los_alumnos':alumno, 'curso':data_curso})


@login_required
def get_alumno(request, string, dni_alumno):
    if request.method == 'POST':
        alumno = Alumno.objects.get(dni=dni_alumno)
        if string == "telefonos":
            print "telefono"
            return render(request, 'templates_cursos/telefonos_alumno.html', {'alumno':alumno})
        else:
            print "otro"
            return render(request, 'templates_cursos/perfil_alumno.html', {'alumno':alumno})
    return HttpResponse("SOlo podes entrar por post")

@login_required
def datos_alumno(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    return render(request, 'perfilAlumno.html', {'alumno':alumno})

@user_passes_test(check_Secretaria)
def docentes(request):
    profesores = Profesor.objects.all()
    return render(request, 'templates_docentes/docentes.html', {'profesores':profesores})

@user_passes_test(check_Secretaria)
def profesor(request, id_profesor):
    profesor = Profesor.objects.get(dni_t=id_profesor)
    return render(request, 'templates_docentes/perfilProfesor.html', {'trabajador':profesor})

@user_passes_test(check_Profesor)
def modificar_profesor(request):
    print request.user
    udocente = user_Docente.objects.get(user__username=request.user)
    return render(request, 'templates_docentes/perfilProfesor.html', {'trabajador':udocente.docente_referenciado})

@login_required
def mi_perfil(request):
    user = User.objects.get(username=request.user)
    if check_Profesor(user):
        udocente = user_Docente.objects.get(user=user)
        trabajador = Profesor.objects.get(dni_t=udocente.docente_referenciado.dni_t)
        return render(request, 'templates_docentes/mi_perfil.html',{'trabajador':trabajador})
    elif check_Director(user):
        udirector = user_Director.objects.get(user=user)
        trabajador = Director.objects.get(dni_t=udirector.director_referenciado.dni_t)
        return render(request, 'templates_docentes/mi_perfil.html',{'trabajador':trabajador})
    elif check_Secretaria(user):
        usecretaria = user_Secretaria.objects.get(user=user)
        trabajador = Secretaria.objects.get(dni_t=usecretaria.secretaria_referenciada.dni_t)
        return render(request, 'templates_docentes/mi_perfil.html',{'trabajador':trabajador})

@login_required
def volver_curso(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    id_curso = alumno.curso.id
    return redirect(cursos3, id_curso)

def formProfesor(request):
    form = ProfesorForm()
    return render(request, 'templates_docentes/formProfesor.html', {'form':form})
