"""
In this file we will see the functions that creates the models for Alumnos, Transportistas and Padres
"""
from django.db import models

def crearAlumno(request):
    if request.method == 'POST':
        alumno_nombre = request.POST['alumno_nombre']
        alumno_apellido = request.POST['alumno_apellido']
        alumno_dni = request.POST['alumno_dni']
        alumno_lugar_nacimiento = request.POST['alumno_lugar_nacimiento']
        alumno_fecha_nacimiento = request.POST['alumno_fecha_nacimiento']
        alumno_domicilio = request.POST['alumno_domicilio']
        alumno_email = request.POST['alumno_email']
        alumno_sexo = request.POST['sexo']
        alumno_telefono_casa = request.POST['alumno_telefono_casa']
        alumno_telefono_padre = request.POST['alumno_telefono_padre']
        alumno_telefono_madre = request.POST['alumno_telefono_madre']
        alumno_telefono_familiar = request.POST['alumno_telefono_familiar']
        alumno_telefono_vecino = request.POST['alumno_telefono_vecino']
        alumno_enfermedad_relevante = request.POST['alumno_enfermedad_relevante']
        alumno_con_quien_vive = request.POST['alumno_con_quien_vive']
        alumno_telefono_que_lo_trae = request.POST['alumno_telefono_que_lo_trae']
        alumno_utiliza_transporte = request.POST['alumno_utiliza_transporte']
        #alumno_transporte = request.POST['alumno_transporte']
        #alumno_autorizados = request.POST['alumno_autorizados']
        #alumno_padres = request.POST['alumno_padres']
        alumno_tiene_obra_social = request.POST['alumno_tiene_obra_social']
        alumno_obra_social_nombre = request.POST['alumno_alumno_tiene_obra_social']
        alumno_obra_social_numero = request.POST['alumno_obra_social_numero']
        alumno_matriculado = request.POST['alumno_matriculado']
    return redirect('formulario')