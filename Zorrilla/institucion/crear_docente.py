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
                try:
                    #Actualizamos la Clave.
                    clave_correcta = clave_Docente.objects.get(clave_logIn=clave, email_docente=email_t, dni_docente=dni_t)
                    clave_correcta.change()
                    clave_correcta.save()
                    form.save()
                    profesor = Trabajador.objects.get(dni_t=dni_t)
                    profesor.cargo_t = "PR"
                    profesor.nombre_t, profesor.apellido_t = profesor.nombre_t.lower(), profesor.apellido_t.lower()
                    profesor.save()
                    password = profesor.create_pass_user()
                    user_d = User.objects.create_user(username=profesor.create_username(), password=password)
                    print (password)
                    my_group = Group.objects.get(name='Profesor')
                    my_group.user_set.add(user_d)
                    profesor.save()
                    user_docente = user_Trabajador(user=user_d, trabajador=profesor)
                    user_docente.save()
                    subject = "Usuario Creado"
                    message = "El Docente " + str(profesor.apellido_t.title()) + "" + str(profesor.nombre_t.title()) + " ha sido ingresado al sistema, en el cual utilizara como nombre de usuario: " + str(user_d.username) + " y la password " + str(password)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email_t]
                    send_mail(subject, message, email_from, recipient_list)
                    data = {
                        'resultado': " Sus datos han sido cargado con exito.",
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
    return HttpResponse("Solo podes acceder por Post")
