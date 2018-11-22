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
                'resultado': " Pedido enviado."
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
    else:
        return HttpResponse("Solo podes entrar por POST")

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
    curso = Curso.objects.filter(hora=aux).order_by('aNo', 'hora','seccion')
    for a in curso:
        a.new_turno()
    data_curso = {
        'turno':turno
    }
    return render(request, 'templates_cursos/cursos2.html', {'todos_los_cursos':curso, 'turno':data_curso})

@login_required
def cursos3(request, id_curso):
    curso = Curso.objects.get(pk=id_curso)
    matriculacion = Matriculacion.objects.filter(curso=curso, matriculado="Si")
    data_curso = {
        'turno':curso.que_turno(),
        'año':curso.aNo,
        'seccion':curso.que_seccion()
}
    return render(request, 'templates_cursos/cursos3.html', {'matriculaciones':matriculacion, 'curso':data_curso})


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
def modificar_perfil(request, dni):
    trabajador = Trabajador.objects.get(dni_t=dni)
    trabajador_elegido = Modificar_Trabajador_Form(initial={'nombre_t':trabajador.nombre_t.title(),'apellido_t':trabajador.apellido_t.title(),'fecha_nacimiento_t':trabajador.fecha_nacimiento_t, 'lugar_nacimiento_t':trabajador.lugar_nacimiento_t.title(), 'domicilio_t':trabajador.domicilio_t.title(), 'email_t':trabajador.email_t,'sexo_t':trabajador.sexo_t,'telefono_particular':trabajador.telefono_particular, 'telefono_laboral':trabajador.telefono_laboral,'telefono_familiar':trabajador.telefono_familiar, 'datos_familiares_cargo':trabajador.datos_familiares_cargo.title(),'antecedentes_laborales':trabajador.antecedentes_laborales.title(), 'estudios_cursados':trabajador.estudios_cursados.title()})
    return render(request, 'templates_docentes/modificarPerfil.html', {'trabajador':trabajador, 'form':trabajador_elegido})

@login_required
def modificar_datos_perfil(request):
    if request.method == "POST":
        form = Modificar_Trabajador_Form(request.POST)
        dni_trabajador = request.POST['dni_user']
        trabajo = request.POST['trabajo']
        print (trabajo)
        user = User.objects.get(username=request.user)
        if form.is_valid():
            trabajador = Trabajador.objects.get(dni_t=dni_trabajador)
            user_T = user_Trabajador.objects.get(trabajador=trabajador)
            if (user_T.user == user):
                nombre = form.cleaned_data['nombre_t']
                apellido = form.cleaned_data['apellido_t']
                nuevo_nombre = nombre.lower()
                nuevo_apellido = apellido.lower()
                nuevo_lugar_nacimiento = form.cleaned_data['lugar_nacimiento_t']
                nueva_fecha_nacimiento = form.cleaned_data['fecha_nacimiento_t']
                nuevo_domicilio = form.cleaned_data['domicilio_t']
                nuevo_email = form.cleaned_data['email_t']
                nuevo_sexo = form.cleaned_data['sexo_t']
                nuevo_telefono_particular = form.cleaned_data['telefono_particular']
                nuevo_telefono_laboral = form.cleaned_data['telefono_laboral']
                nuevo_telefono_familiar = form.cleaned_data['telefono_familiar']
                nuevo_datos_familiares_cargo = form.cleaned_data['datos_familiares_cargo']
                nuevo_antecedentes_laborales = form.cleaned_data['antecedentes_laborales']
                nuevo_estudios_cursados = form.cleaned_data['estudios_cursados']
                trabajador.nombre_t, trabajador.apellido_t, trabajador.lugar_nacimiento_t, trabajador.fecha_nacimiento_t, trabajador.domicilio_t, trabajador.email_t, trabajador.sexo_t, trabajador.telefono_particular,trabajador.telefono_laboral, trabajador.telefono_familiar, trabajador.datos_familiares_cargo, trabajador.antecedentes_laborales, trabajador.estudios_cursados = nuevo_nombre, nuevo_apellido, nuevo_lugar_nacimiento, nueva_fecha_nacimiento, nuevo_domicilio, nuevo_email, nuevo_sexo, nuevo_telefono_particular, nuevo_telefono_laboral, nuevo_telefono_familiar, nuevo_datos_familiares_cargo, nuevo_antecedentes_laborales, nuevo_estudios_cursados
                trabajador.save()
                subject = "Perfil Modificado"
                message = "Se le notifica que se han realizado cambios en su perfil de " + str(trabajo) + " dentro del Sistema."
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [nuevo_email]
                send_mail( subject, message, email_from, recipient_list )
                data = {
                    'error':False,
                    'resultado': " Perfil Modificado con Exito."
                }
                print ("es valido")
                return JsonResponse(data)

            else:
                data = {
                    'error':True,
                    'resultado': "Error el Perfil no corresponde con el Usuario Actual."
                }
                return JsonResponse(data)
        else:
            data = {
                'error':True,
                'resultado': str(form.errors)
            }
            return JsonResponse(data)
    else:
        return HttpResponse("Solo podes entrar por post")

@login_required
def mi_perfil(request):
    user = User.objects.get(username=request.user)
    u_trabajador = user_Trabajador.objects.get(user=user)
    trabajador = u_trabajador.trabajador
    return render(request, 'templates_docentes/mi_perfil.html', {'trabajador':trabajador})

@login_required
def volver_curso(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    matriculacion = Matriculacion.objects.get(alumno=alumno)
    return redirect(cursos3, matriculacion.curso.id)

def formProfesor(request):
    form = ProfesorForm()
    return render(request, 'templates_docentes/formProfesor.html', {'form':form})
