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


class Profesor(Persona):
    foto = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    telefono_particular_p = models.IntegerField(max_length=15)
    telefono_laboral_p = models.IntegerField(max_length=15)
    telefono_familiar_p = models.IntegerField(max_length=15)
    datos_familiares_cargo = models.TextArea(max_length=300)
    fecha_inicio_actividad = models.DateTimeField()
    antecedentes_laborales = models.TextArea(max_length=300)
    antiguedad_en_empresa = models.DateTimeField()
    estudios_cursados = models.TextArea(max_length=300)
