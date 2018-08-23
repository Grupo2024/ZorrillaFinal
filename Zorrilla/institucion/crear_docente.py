from django.db import models
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from matriculacion.models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group


def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        clave = request.POST['profesor_clave']
        print clave + " clave"
        if form.is_valid():
            nombre_t = form.cleaned_data['nombre_t']
            apellido_t = form.cleaned_data['apellido_t']
            dni_t = form.cleaned_data['dni_t']
            fecha_nacimiento_t = form.cleaned_data['fecha_nacimiento_t']
            lugar_nacimiento_t = form.cleaned_data['lugar_nacimiento_t']
            domicilio_t = form.cleaned_data['domicilio_t']
            email_t = form.cleaned_data['email_t']
            sexo_t = form.cleaned_data['sexo_t']
            telefono_particular = form.cleaned_data['telefono_particular']
            telefono_laboral = form.cleaned_data['telefono_laboral']
            telefono_familiar = form.cleaned_data['telefono_familiar']
            datos_familiares_cargo = form.cleaned_data['datos_familiares_cargo']
            antecedentes_laborales = form.cleaned_data['antecedentes_laborales']
            estudios_cursados = form.cleaned_data['estudios_cursados']
            profesor = Profesor(nombre_t=nombre_t, apellido_t=apellido_t, dni_t=dni_t, fecha_nacimiento_t=fecha_nacimiento_t
            , lugar_nacimiento_t=lugar_nacimiento_t, domicilio_t=domicilio_t, email_t=email_t, sexo_t=sexo_t, telefono_particular=telefono_particular, telefono_laboral=telefono_laboral, telefono_familiar=telefono_familiar, datos_familiares_cargo=datos_familiares_cargo, antecedentes_laborales=antecedentes_laborales, estudios_cursados=estudios_cursados)
            print profesor
            try:
                cdocente = clave_Docente.objects.get(clave_logIn=clave, email_docente=email_t, dni_docente=dni_t)
                cdocente.change()
                cdocente.save()
                password = profesor.create_pass_user()
                user_d = User.objects.create_user(username=profesor.create_username(), password=password)
                print password
                my_group = Group.objects.get(name='Profesor') 
                my_group.user_set.add(user_d)
                profesor.save()
                user_docente = user_Docente(user=user_d, docente_referenciado=profesor)
                user_docente.save()
                subject = "Usuario Creado"
                message = "El Docente " + str(profesor.apellido_t) + "" + str(profesor.nombre_t) + " ha sido ingresado al sistema, en el cual utilizara como nombre de usuario: " + str(user_d.username) + " y la password " + str(password)
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email_t]
                send_mail(subject, message, email_from, recipient_list)
                data = {
                    'resultado': "El docente " + str(apellido_t) + "" + str(nombre_t) + " ha sido cargado con exito.",
                    'nombre': nombre_t,
                    'apellido': apellido_t,
                    'dni': dni_t,
                    'username': profesor.create_username(),
                    'password': password,
                    'error': False
                }
                print "No hay error"
                return JsonResponse(data)
            except clave_Docente.DoesNotExist:
                print "No coincide la clave"
                data = {
                    'resultado': "La clave no coincide con esa direccion de Email-Dni",
                    'error': True
                }
                return JsonResponse(data)
        data = {
            'error': True,
            'resultado': str(form.errors)
        }
        return JsonResponse(data)
