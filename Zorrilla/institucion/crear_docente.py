from django.db import models
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.utils import timezone
from matriculacion.models import *

def crear_Profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        clave = request.POST['profesor_clave']
        print clave
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
            fecha_inicio_actividad = form.cleaned_data['fecha_inicio_actividad']
            antecedentes_laborales = form.cleaned_data['antecedentes_laborales']
            estudios_cursados = form.cleaned_data['estudios_cursados']
            profesor = Profesor(nombre_t=nombre_t, apellido_t=apellido_t, dni_t=dni_t, fecha_nacimiento_t=fecha_nacimiento_t
            , lugar_nacimiento_t=lugar:nacimiento_t, domicilio_t=domicilio_t, email_t=email_t, sexo_t=sexo_t, telefono_particular=telefono_particular, telefono_laboral=telefono_laboral, telefono_familiar=telefono_familiar, datos_familiares_cargo=datos_familiares_cargo, fecha_inicio_actividad=fecha_inicio_actividad, antecedentes_laborales=antecedentes_laborales, antecedentes_laborales=antecedentes_laborales, estudios_cursados=estudios_cursados)
            cdocente = clave_Docente.objects.get(dni_docente=profesor.dni_t, email_docente=profesor.email_t, clavelogIn=clave)
            if cdocente:
                cdocente.ingresado = True
                cdocente.save()
                user_d = User.objects.create_user(username=profesor.create_password_user(1), email=profesor.create_password_user(2))
                user_d.save()
                profesor.save()
                user_docente = user_Docente(user=user_d, docente_referenciado=profesor)
                user_docente.save()
                