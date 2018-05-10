from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.AutoField(primary_key=True)
    lugar_nacimiento = models.CharField(max_length=150)
    fecha_nacimiento = models.DateTimeField()
    domicilio = models.CharField(max_length=150)
    email = models.EmailField(max_length=70, blank=True)
    #Datos estandares de persona, estos van a ser heredados x cualquier profesor o alumno

    def __str__(self):
        return 'Persona: {} {}| dni: {}| '.format(self.nombre,
         self.apellido, self.dni)

    class Meta:
        abstract = True


class Profesor(Persona)
    foto 
    telefono_particular_p
    telefono_laboral_p
    telefono_familiar_p
    datos_familiares_cargo
    fecha_inicio_actividad
    antecedentes_laborales
    antiguedad_en_empresa
    antiguedad_en_escuela