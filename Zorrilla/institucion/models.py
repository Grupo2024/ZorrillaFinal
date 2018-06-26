# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from matriculacion.models import *

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

class Director(Profesor):
    
    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)


class Secretaria(Profesor):

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)


class Turno(models.Model):
    hora = models.BooleanField('Clickea para seleccionar turno "Tarde"', null=False)

    def que_hora(self):
        aux = 'Maniana'
        if self.hora:
            aux = 'Tarde'
            return aux
        else:
            return aux

    def __str__(self):
        return 'Turno {}'.format(self.que_hora())



class Grado(models.Model):
    aNo = models.CharField('1ero, 2do, etc...', max_length=5)
    turno_asignado = models.ForeignKey(Turno, null=False)

    def __str__(self):
        return 'El Grado {} asiste al turno {}'.format(self.aNo, self.turno_asignado.que_hora())


class Seccion(models.Model):
    curso = models.CharField('A-B-C-D', max_length=1)
    prof_asignado = models.ForeignKey(Profesor, null=False)
    grado_asignado = models.ForeignKey(Grado, null=False)

    def __str__(self):
       return 'El curso {} {} turno {} tiene como profesor asignado a {} {}'.format(self.curso, self.grado_asignado.aNo, self.grado_asignado.turno_asignado.que_hora, self.prof_asignado.apellido, self.prof_asignado.nombre)
