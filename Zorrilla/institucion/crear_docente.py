"""
In this file we will see the functions that creates the models for profesors, Transportistas and Padres
"""
from django.db import models
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from matriculacion.models import *

def crear_profesor(request):
    print "LLego"
    if request.method == 'POST':
        profesor_nombre = request.POST['profesor_nombre']
        profesor_apellido = request.POST['profesor_apellido']
        profesor_dni = request.POST['profesor_dni']
        profesor_lugar_nacimiento = request.POST['profesor_lugar_nacimiento']
        profesor_fecha_nacimiento = request.POST['profesor_fecha_nacimiento']
        profesor_domicilio = request.POST['profesor_domicilio']
        profesor_mail = request.POST['profesor_mail']
        gender = request.POST['gender']

        profesor_telefono_particular_p = request.POST['profesor_telefono_particular_p']
        profesor_telefono_laboral_p = request.POST['profesor_telefono_laboral_p']
        profesor_telefono_familiar_p = request.POST['profesor_telefono_familiar_p']
        profesor_datos_familiares_cargo = request.POST['profesor_datos_familiares_cargo']

        profesor_fecha_inicio_actividad = request.POST['profesor_fecha_inicio_actividad']
        profesor_antecedentes_laborales = request.POST['profesor_antecedentes_laborales']
        profesor_antiguedad_en_empresa = request.POST['profesor_antiguedad_en_empresa']
        profesor_estudios_cursados = request.POST['profesor_estudios_cursados']
        profesor1 = Profesor(nombre=profesor_nombre,
                             apellido=profesor_apellido,
                             dni=profesor_dni,
                             lugar_nacimiento=profesor_lugar_nacimiento,
                             fecha_nacimiento=profesor_fecha_nacimiento,
                             domicilio=profesor_domicilio,
                             email=profesor_mail,
                             sexo=gender,
                             telefono_particular_p = profesor_telefono_particular_p,
                             telefono_laboral_p=profesor_telefono_laboral_p,
                             telefono_familiar_p=profesor_telefono_familiar_p,
                             datos_familiares_cargo=profesor_datos_familiares_cargo,
                             fecha_inicio_actividad=profesor_fecha_inicio_actividad,
                             antecedentes_laborales=profesor_antecedentes_laborales,
                             antiguedad_en_empresa=profesor_antiguedad_en_empresa,
                             estudios_cursados=profesor_estudios_cursados)
        profesor1.save()
        return redirect('docentes')