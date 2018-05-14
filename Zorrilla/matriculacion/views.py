from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    alumno = Alumno.objects.get(nombre="Gonzalo")
    print "Mostramos los datos del Alumno:"
    print "==============================="
    print "Nombre"
    print alumno.nombre
    print "apellido"
    print alumno.apellido
    print "Dni"
    print alumno.dni
    print "Lugar Nacimiento"
    print alumno.lugar_nacimiento
    print "Fecha Nacimiento"
    print alumno.fecha_nacimiento
    print "Domicilio"
    print alumno.domicilio
    print "Email"
    print alumno.email
    print "Sexo"
    print alumno.sexo
    print "Telefono Casa"
    print alumno.telefono_casa
    print "Telefono Padre"
    print alumno.telefono_padre
    print "Telefono Madre"
    print alumno.telefono_madre
    print "Telefono Familiar"
    print alumno.telefono_familiar
    print "Telefono Vecino"
    print alumno.telefono_vecino
    print "Enfermedad Relevante"
    print alumno.enfermedad_relevante
    print "Con Quien Vive"
    print alumno.con_quien_vive
    print "Quien lo treae ?"
    print alumno.quien_lo_trae
    print "Utiliza transporte"
    print alumno.utiliza_transporte
    print "Transorte"
    print alumno.transporte
    print "Autorizados"
    print alumno.autorizados
    print "Padres"
    print alumno.padres
    print "tiene_obra_social"
    print alumno.tiene_obra_social
    print "obra social"
    print alumno.obra_social_nombre
    print "obra_social_numero"
    print alumno.obra_social_numero
    return render(request, 'index.html')
