# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from matriculacion.models import *

# Create your models here.

class Director(Profesor):
    
    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)


class Secretaria(Profesor):

    def __str__(self):
        return 'Persona: {} {}| dni: {}| sexo: {}'.format(self.nombre, self.apellido, self.dni, self.sexo)


class Turno(models.Model):
    hora = models.BooleanField('Clickea para seleccionar turno "Tarde"', null=False)

    def que_hora(self):
        aux = 'Mañana'
        if self.hora:
            aux = 'Tarde'
            return aux
        else:
            return aux



class Grado(models.Model):
    aNo = models.CharField('1ero, 2do, etc...', max_length=5)
    turno_asignado = models.ForeignKey(Turno, null=False)


class Seccion(models.Model):
    curso = models.CharField('A-B-C-D', max_length=1)
    prof_asignado = models.ForeignKey(Profesor, null=False)
    grado_asignado = models.ForeignKey(Grado, null=False)

#    def __str__(self):
#       return ''.format(self.alumno.nombre, self.matriculado)