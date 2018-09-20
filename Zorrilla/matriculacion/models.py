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


class Transportista(Persona):
    nombre_transporte = models.CharField('Nombre del Transporte', max_length=40)
    telefono_transportista = models.IntegerField('Telefono del Transportista')
    detalles_transportista = models.TextField('Detalles del Transportista', max_length=300)

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)


class Obra_Social(models.Model):
    obra_social_nombre = models.CharField('Nombre Obra Social', max_length=40, null=True)

    def __str__(self):
        return 'Obra Social: {}'.format(self.obra_social_nombre)


class Padre_madre(Persona):
    profesion = models.CharField('Profesion del Padre/Madre', max_length=40)
    telefono_trabajo = models.IntegerField('Telefono del Trabajo del Padre/Madre')

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)


class Alumno(Persona):
    telefono_casa = models.IntegerField('Telefono de la Casa')
    telefono_padre = models.IntegerField('Telefono del Padre', null=True)
    telefono_madre = models.IntegerField('Telefono de la Madre', null=True)
    telefono_familiar = models.IntegerField('Telefono de algun Familiar', null=True)
    telefono_vecino = models.IntegerField('Telefono de algun Vecino', null=True)
    enfermedad_relevante = models.CharField('Enfermedad relevante', max_length=40, null=True)
    con_quien_vive = models.CharField('Con quien vive', max_length=40)
    quien_lo_trae = models.CharField('Quien lo trae', max_length=40)
    telefono_que_lo_trae = models.IntegerField('Telefono de quien lo trae')
    padres = models.ForeignKey(Padre_madre)

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)


class Autorizado(Persona):
    telefono_autorizado = models.IntegerField('Telefono del autorizado')
    relacion_con_alumno = models.TextField('Que relacion tiene con el alumno', max_length=300)
    alumno = models.ForeignKey(Alumno, null=False)

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)    
'''
    Esta clase autorizado, esta hecha para las personas que no sean padre, madre o transportista
    y puedan retirar al alumno, se requiere aclarar la relacion entre esta persona y el alumno
    en cuestion.
''' 


class Matriculacion(models.Model):
    alumno = models.ForeignKey(Alumno, null=False)
    fecha_matriculacion = models.DateTimeField('Fecha Matriculacion', blank=True)
    matriculado = models.BooleanField('Esta matriculado o no', default=False)

    def __str__(self):
        return 'El alumno: {} tiene un estado de matriculacion {}'.format(self.alumno.nombre, self.matriculado)


'''
    Ahora vienen todas clases intermedias, para hacer que la relacion entre estas, 
    y alumno, sea de muchos a muchos 
'''


class usa_Transporte(models.Model):
    alumno = models.ForeignKey(Alumno, null=False)
    transportista = models.ForeignKey(Transportista, null=False)
    #Tqm sr Bracha

    def __str__(self):
        return 'El alumno: {} utiliza el transportista: {}'.format(self.alumno.nombre, self.transportista.nombre_transporte)


class usa_Obra_Social(models.Model):
    alumno = models.ForeignKey(Alumno, null=False)
    obra_social = models.ForeignKey(Obra_Social, null=False)
    obra_social_numero = models.IntegerField('Num Obra Social', null=False)#Numero de afiliacion a la obra social


class Asignacion_Alumno(models.Model):
    curso = models.ForeignKey(Curso, null=False)
    alumno = models.ForeignKey(Alumno, null=False)

    def __str__(self):
       return 'Alumno {} {} asiste al curso: {} {} turno {}'.format(self.alumno.nombre, self.alumno.apellido, self.curso.aNo, self.curso.seccion.que_seccion, self.curso.turno_asignado.que_hora())
