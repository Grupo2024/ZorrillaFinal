# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from matriculacion.models import *

from django.contrib.auth.models import User #Para el user

# Create your models here.

class clave_Docente(models.Model):
    clave_logIn = models.CharField(null=False, max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    email_docente = models.EmailField(null=False)
    dni_docente = models.IntegerField(null=False)
    ingresado = models.BooleanField(default=False)#False hasta que se ingrese el docente al sistema.
    
    def change(self):
        if self.ingresado:
            self.ingresado = False
            self.save()
            return self.ingresado
        else:
            self.ingresado = True
            self.save()
            return self.ingresado


# Create your models here.

class Trabajador(models.Model):
    nombre_t = models.CharField('Nombre del trabajador', max_length=40)
    apellido_t = models.CharField('Apellido del trabajador', max_length=40)
    dni_t = models.IntegerField('Dni del trabajador', primary_key=True)
    lugar_nacimiento_t = models.CharField('Lugar de Nacimiento', max_length=150, blank=True)
    fecha_nacimiento_t = models.DateField('Fecha Nacimiento', blank=True)
    domicilio_t = models.CharField('Domicilio del trabajador', max_length=150, blank=True)
    email_t = models.EmailField('Email del trabajador', max_length=70, blank=True)
    sexo_t = models.BooleanField('Sexo del trabajador(True = Hombre)', null = False)#True = Hombre, False = Madre
    #Datos estandares del trabajador, estos van a ser heredados x cualquier profesor, director o secretaria
    #foto = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    #BUSCAR LO DE FOTOS
    telefono_particular = models.IntegerField('Telefono Personal del Trabajador')
    telefono_laboral = models.IntegerField('Telefono Laboral del Trabajador')
    telefono_familiar = models.IntegerField('Telefono de algun Familiar del Trabajador')
    datos_familiares_cargo = models.TextField('Nombre y Apellido de familiar del Trabajador', max_length=300)
    fecha_inicio_actividad = models.DateField('Fecha de Inicio de Clases en el Colegio')
    antecedentes_laborales = models.TextField('Datos de Trabajos Previos', max_length=300)
    antiguedad_en_empresa = models.DateField('Antiguedad en la Empresa')
    estudios_cursados = models.TextField('Estudios del Trabajador', max_length=300)

    def genero(self):
        aux = 'Mujer'
        if self.sexo_t:
            aux = 'Hombre'
            return aux
        else:
            return aux
    '''
    Me crea la variable auxiliar, que por default es mujer, si se marca como true, me devuelve que
    es un hombre, sino, quedara como mujer
    '''

    def __str__(self):
        return 'Trabajador: {} {}| dni: {}| sexo: {}'.format(self.nombre_t,
         self.apellido_t, self.dni_t, self.genero())

    class Meta:
        abstract = True


class Profesor(Trabajador):

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre_t, self.apellido_t, self.dni_t, self.sexo_t)


class Director(Trabajador):

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre_t, self.apellido_t, self.dni_t, self.sexo_t)


class Secretaria(Trabajador):

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre_t, self.apellido_t, self.dni_t, self.sexo_t)


class Curso(models.Model):
    hora = models.BooleanField('Clickea para seleccionar turno "Tarde"', null=False)
    aNo = models.CharField('1ero, 2do, etc...', max_length=5)
    seccion = models.BooleanField('True = B o D, dependiendo de si es turno mañana o tarde', null=False)

    def que_turno(self):
        aux = 'Maniana'
        if (self.hora == True):
            aux = 'Tarde'
            return aux
        else:
            return aux

    def que_seccion(self):
        if (self.hora == True):
            aux = 'C'
            if (self.seccion == True):
                aux = 'D'
                return aux
            else:
                return aux
        else:
            aux = 'A'
            if (self.seccion == True):
                aux = 'B'
                return aux
            else:
                return aux

    def new_turno(self):
        if self.hora:
            self.turno = "Tarde"
        else:
            self.turno = "Maniana"
        return self.turno

    def __str__(self):
        return 'El Grado {} {} asiste al turno {}'.format(self.aNo, self.que_seccion() ,self.que_turno())



class Asignacion(models.Model):
    prof_asignado = models.ForeignKey(Profesor)
    curso = models.ForeignKey(Curso)

    def __str__(self):
       return 'El profesor {} {} asiste al curso: {} {} turno {}'.format(self.prof_asignado.nombre_t, self.prof_asignado.apellido_t, self.curso.aNo, self.curso.seccion.que_seccion, self.curso.turno_asignado.que_hora())



class user_Docente(models.Model):
    user = models.OneToOneField(User)
    docente_referenciado = models.OneToOneField(Profesor, on_delete=models.CASCADE)

class user_Secretaria(models.Model):
    user = models.OneToOneField(User)
    secretaria_referenciada = models.OneToOneField(Secretaria, on_delete=models.CASCADE)

class user_Director(models.Model):
    user = models.OneToOneField(User)
    director_referenciado = models.OneToOneField(Director, on_delete=models.CASCADE)
