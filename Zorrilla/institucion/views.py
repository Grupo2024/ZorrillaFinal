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
            print ("es valido")
            return JsonResponse(data)
        else:
            print ("No es valido")
            print (form.errors)
            data = {
                'error':True,
                'resultado': str(form.errors)
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
    print (turno)
    if turno == "Maniana":
        aux = False
    else:
        aux = True
    curso = Curso.objects.filter(hora=aux).order_by('aNo')
    for a in curso:
        a.new_turno()

    data_curso = {
        'turno':turno
    }
    return render(request, 'templates_cursos/cursos2.html', {'todos_los_cursos':curso, 'turno':data_curso})

@login_required
def cursos3(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    alumnos_curso = alumno_Curso.objects.filter(curso=curso)
    data_curso = {
        'turno':curso.que_turno(),
        'año':curso.aNo,
        'seccion':curso.que_seccion()
    }
    return render(request, 'templates_cursos/cursos3.html', {'alumnos_curso':alumnos_curso, 'curso':data_curso})


@login_required
def get_alumno(request, string, dni_alumno):
    if request.method == 'POST':
        alumno = Alumno.objects.get(dni=dni_alumno)
        if string == "telefonos":
            print ("telefono")
            return render(request, 'templates_cursos/telefonos_alumno.html', {'alumno':alumno})
        else:
            print ("otro")
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
    return render(request, 'templates_docentes/perfilDocente.html', {'trabajador':profesor})

@login_required
def modificar_perfil(request, clase, dni):
    if (clase == "Secretaria"):
        trabajador_elegido = Secretaria.objects.get(dni_t=dni)
    elif (clase == "Director"):
        trabajador_elegido = Director.objects.get(dni_t=dni)
    else:
        trabajador_elegido = Profesor.objects.get(dni_t=dni)
    ln = trabajador_elegido.lugar_nacimiento_t
    trabajador = ModificarForm(initial={'nombre':trabajador_elegido.nombre_t,
                                        'apellido':trabajador_elegido.apellido_t,
                                        'lugar_nacimineto':trabajador_elegido.nombre_t,
                                        'fecha_nacimiento':trabajador_elegido.fecha_nacimiento_t,
                                        'domicilio':trabajador_elegido.domicilio_t,
                                        'email':trabajador_elegido.email_t,
                                        'sexo':trabajador_elegido.sexo_t,
                                        'telefono_particular':trabajador_elegido.telefono_particular, 'telefono_laboral':trabajador_elegido.telefono_laboral, 'telefono_familiar':trabajador_elegido.telefono_familiar, 'datos_familiares_cargo':trabajador_elegido.datos_familiares_cargo, 'fecha_inicio_actividad':trabajador_elegido.fecha_inicio_actividad,
                                        'antecedentes_laborales':trabajador_elegido.antecedentes_laborales, 'estudios_cursados':trabajador_elegido.estudios_cursados})
    return render(request, 'templates_docentes/modificarPerfil.html', {'trabajador':trabajador, 'trabajador_elegido':trabajador_elegido})

@login_required
def mi_perfil(request):
    user = User.objects.get(username=request.user)
    if check_Profesor(user):
        udocente = user_Docente.objects.get(user=user)
        trabajador = Profesor.objects.get(dni_t=udocente.docente_referenciado.dni_t)
        trabajador.cargo = "Profesor"
        return render(request, 'templates_docentes/mi_perfil.html',{'trabajador':trabajador})
    elif check_Director(user):
        udirector = user_Director.objects.get(user=user)
        trabajador = Director.objects.get(dni_t=udirector.director_referenciado.dni_t)
        trabajador.cargo = "Director"
        return render(request, 'templates_docentes/mi_perfil.html',{'trabajador':trabajador})
    elif check_Secretaria(user):
        usecretaria = user_Secretaria.objects.get(user=user)
        trabajador = Secretaria.objects.get(dni_t=usecretaria.secretaria_referenciada.dni_t)
        trabajador.cargo = "Secretaria"
        return render(request, 'templates_docentes/mi_perfil.html',{'trabajador':trabajador})

@login_required
def volver_curso(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    id_curso = alumno.curso.id
    return redirect(cursos3, id_curso)

def formProfesor(request):
    form = ProfesorForm()
    return render(request, 'templates_docentes/formProfesor.html', {'form':form})
