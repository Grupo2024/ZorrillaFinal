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
        clave = request.POST['profesor_clave']
        try:
            existe_clave = clave_Docente.objects.get(clave_logIn=clave)
            form = ProfesorForm(request.POST)
            if form.is_valid():
                dni_t = form.cleaned_data['dni_t']
                email_t = form.cleaned_data['email_t']
                print email_t
                try:
                    #Actualizamos la Clave.
                    clave_correcta = clave_Docente.objects.get(clave_logIn=clave, email_docente=email_t, dni_docente=dni_t)
                    clave_correcta.change()
                    clave_correcta.save()
                    form.save()
                    profesor = Profesor.objects.get(dni_t=dni_t)
                    password = profesor.create_pass_user()
                    #Creamos el Usuario
                    user_d = User.objects.create_user(username=profesor.create_username(), password=password)
                    print (password)
                    #Lo agregamos al grupo Profesor.
                    my_group = Group.objects.get(name='Profesor')
                    my_group.user_set.add(user_d)
                    profesor.save()
                    #Creamos la Clase intermedia.
                    user_docente = user_Docente(user=user_d, docente_referenciado=profesor)
                    user_docente.save()
                    #Email Notificando la creacion del usuario.
                    subject = "Usuario Creado"
                    message = "El Docente " + str(profesor.apellido_t) + "" + str(profesor.nombre_t) + " ha sido ingresado al sistema, en el cual utilizara como nombre de usuario: " + str(user_d.username) + " y la password " + str(password)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email_t]
                    send_mail(subject, message, email_from, recipient_list)
                    data = {
                        'resultado': "El docente " + str(profesor.apellido_t) + "" + str(profesor.nombre_t) + " ha sido cargado con exito.",
                        'nombre': profesor.nombre_t,
                        'apellido': profesor.apellido_t,
                        'dni': profesor.dni_t,
                        'username': profesor.create_username(),
                        'password': password,
                        'error': False
                    }
                    print ("No hay error")
                    return JsonResponse(data)
                #La Clave no coincide con el Dni.
                except clave_Docente.DoesNotExist:
                    data = {
                        'error':True,
                        'resultado': "La Clave no coincide con ese Dni-Email."
                    }
                    return JsonResponse(data)
            #No es valido
            else:
                data = {
                    'error':True,
                    'resultado': str(form.errors)
                }
                return JsonResponse(data)

        #No existe esa clave.
        except clave_Docente.DoesNotExist:
            data = {
                'error':True,
                'resultado': "No existe un pedido que contenga esta clave."
            }
            return JsonResponse(data)

