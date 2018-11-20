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
    lugar_nacimiento = models.CharField('Lugar de Nacimiento', max_length=150, null=False)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', default="2000-10-10")
    domicilio = models.CharField('Domicilio', max_length=150, null=False)
    email = models.EmailField('Email', max_length=70, null=False)
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
    nombre = models.CharField('Nombre Obra Social', max_length=40, unique=True)

    def __str__(self):
        return 'Obra Social: {}'.format(self.nombre)


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

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)


class Autorizado(Persona):
    telefono_autorizado = models.IntegerField('Telefono del autorizado')

    def __str__(self):
        return 'Persona: {} {}| dni: {}|'.format(self.nombre, self.apellido, self.dni)    
'''
    Esta clase autorizado, esta hecha para las personas que no sean padre, madre o transportista
    y puedan retirar al alumno, se requiere aclarar la relacion entre esta persona y el alumno
    en cuestion.
''' 


class Matriculacion(models.Model):

    SI = 'Si'
    NO = 'No'
    RE = 'Re'
    EG = 'Eg'
    PE = 'Pe'

    #RE = Re Matricular
    #EG = Egresado
    #PE = Por Egresar

    MATRICULACION_CHOICES = (
        (SI , 'Si'),
        (NO , 'No'),
        (RE, 'Re'),
        (EG, 'Eg'),
        (PE, 'Pe')
    )

    alumno = models.ForeignKey(Alumno, null=False)
    fecha_matriculacion = models.DateTimeField('Fecha Matriculacion', auto_now_add=True)
    matriculado = models.CharField('Estado', max_length=2, choices=MATRICULACION_CHOICES)
    curso = models.ForeignKey(Curso, null=True)

    def __str__(self):
        return 'El alumno: {} tiene un estado de matriculacion {}'.format(self.alumno.nombre, self.matriculado)


'''
    Ahora vienen todas clases intermedias, para hacer que la relacion entre estas, 
    y alumno, sea de muchos a muchos 
'''


class Familia(models.Model):
    alumno = models.ForeignKey(Alumno, null=False)
    padre_madre = models.ForeignKey(Padre_madre, null=False)
    fecha_relacion = models.DateTimeField(auto_now_add=True)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return '{} - {}'.format(self.padre_madre.nombre, self.alumno.nombre)


class usa_Transporte(models.Model):
    alumno = models.ForeignKey(Alumno, null=False)
    transportista = models.ForeignKey(Transportista, null=False)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return 'El alumno: {} utiliza el transportista: {}'.format(self.alumno.nombre, self.transportista.nombre_transporte)


class usa_Obra_Social(models.Model):
    alumno = models.ForeignKey(Alumno, null=False)
    obra_social = models.ForeignKey(Obra_Social, null=False)
    habilitado = models.BooleanField(default=True)
    numero_afiliado = models.IntegerField('Num Obra Social', null=False)#Numero de afiliacion a la obra social

    def __str__(self):
        return 'El alumno {} utiliza la obra social {}'.format(self.alumno.nombre, self.obra_social.nombre)

class alumno_Autorizado(models.Model):
    relacion_con_alumno = models.TextField('Que relacion tiene con el alumno', max_length=50, null=False)
    alumno = models.ForeignKey(Alumno, null=False)
    autorizado = models.ForeignKey(Autorizado, null=False)
    habilitado = models.BooleanField(default = True)
    
    def __str__(self):
        return '{} {} - {} {}'.format(self.alumno.apellido, self.alumno.nombre, self.autorizado.nombre, self.autorizado.apellido)

class datos_Index(models.Model):
    telefono = models.IntegerField(null=False)
    telefono2 = models.IntegerField(null=False)
    email = models.EmailField(null=False)
    email2 = models.EmailField(null=False)
    latitud = models.IntegerField(null=False)
    longitud = models.IntegerField(null=False)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.telefono, self.telefono2, self.email,self.email2, self.latitud, self.longitud)
