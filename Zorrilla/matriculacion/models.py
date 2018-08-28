from __future__ import unicode_literals
from django.db import models

from institucion.models import *

# Create your models here.

class Persona(models.Model):
    
    HO = 'Hombre'
    MU = 'Mujer'
    
    GENERO_CHOICES = (
        (HO , 'Hombre'),
        (MU , 'Mujer'),
    )
    
    nombre = models.CharField('Nombre', max_length=40)
    apellido = models.CharField('Apellido', max_length=40)
    dni = models.IntegerField('Dni', primary_key=True)
    lugar_nacimiento = models.CharField('Lugar de Nacimiento', max_length=150, blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', default="2000-10-10")
    domicilio = models.CharField('Domicilio', max_length=150, blank=True)
    email = models.EmailField('Email', max_length=70, blank=True)
    sexo = models.CharField('Sexo', max_length=6, choices=GENERO_CHOICES)

    #Datos estandares de persona, estos van a ser heredados x cualquier profesor o alumno

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre,
         self.apellido, self.dni, self.sexo)

    class Meta:
        abstract = True


class Autorizado(Persona):
    autorizacion = models.BooleanField('Esta autorizado o no')

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)



class Transportista(Persona):
    nombre_transporte = models.CharField('Nombre del Transporte', max_length=40)
    telefono_transportista = models.IntegerField('Telefono del Transportista')
    detalles_transportista = models.TextField('Detalles del Transportista', max_length=300)

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)



class Padre_madre(Persona):
    profesion = models.CharField('Profesion del Padre/Madre', max_length=40)
    telefono_trabajo = models.IntegerField('Telefono del Trabajo del Padre/Madre')

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)



class Alumno(Persona):
    curso = models.ForeignKey(Curso, blank=True)
    telefono_casa = models.IntegerField('Telefono de la Casa')
    telefono_padre = models.IntegerField('Telefono del Padre', null=True)
    telefono_madre = models.IntegerField('Telefono de la Madre', null=True)
    telefono_familiar = models.IntegerField('Telefono de algun Familiar', null=True)
    telefono_vecino = models.IntegerField('Telefono de algun Vecino', null=True)
    enfermedad_relevante = models.CharField('Enfermedad relevante', max_length=40, null=True)
    con_quien_vive = models.CharField('Con quien vive', max_length=40)
    quien_lo_trae = models.CharField('Quien lo trae', max_length=40)
    telefono_que_lo_trae = models.IntegerField('Telefono de quien lo trae')
    autorizados = models.ForeignKey(Autorizado, blank=True, null=True)
    padres = models.ForeignKey(Padre_madre)
    tiene_obra_social = models.BooleanField('Tiene obra o no')
    obra_social_nombre = models.CharField('Nombre Obra Social', max_length=40, null=True)
    obra_social_numero = models.IntegerField('Num Obra Social')#Numero de afiliacion a la obra social
    matriculado = models.BooleanField('Esta matriculado o no')

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)

    def matricular(self):
        if self.matriculado is not False:
            self.matriculado = True
        return self.matriculado



#Voy a crear una clase intermedia entre alumnos y transportista, para hacer que la relacion
# entre estas 2 clases, sea de Muchos a Muchos
class usa_Transporte(models.Model):
    alumnx = models.ForeignKey(Alumno, null=False)
    transportistx = models.ForeignKey(Transportista, null=False)
    #Tqm sr Bracha

    def __str__(self):
        return 'El alumno: {} utiliza el transportista: {}'.format(self.alumnx.nombre, self.transportistx.nombre_transporte)



class Matriculacion(models.Model):
    alumno = models.ForeignKey(Alumno, null=False)
    fecha_matriculacion = models.DateTimeField('Fecha Matriculacion', blank=True)
    matriculado = models.BooleanField('Esta matriculado o no', default=False)

    def __str__(self):
        return 'El alumno: {} tiene un estado de matriculacion {}'.format(self.alumno.nombre, self.matriculado)
