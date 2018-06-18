# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    title = models.CharField(max_length=60, blank=False)
    tipo = models.CharField('Libro, Texto, Ejercicios, etc', max_length=50)
    autor = models.CharField(max_length=120)
    editorial = models.CharField(max_length=120, null=True)
    fecha_lanzamiento = models.DateTimeField(null=True)
    cantidad_paginas = models.IntegerField(null=True)
    genero = models.CharField(max_length=60, null=True)
    habilitado = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Titulo {}, id {}'.format(self.title, self.id)

    def change(self):
        if self.habilitado:
            self.habilitado = False
            self.save()
            return self.habilitado
        else:
            self.habilitado = True
            self.save()
            return self.habilitado
        
class Estado(models.Model):

    HA = 'Habilitar'
    DH = 'Deshabilitar'
    EL = 'Eliminar'
    CR = 'Crear'
    ED = 'Editar'

    MODIFICACION_CHOICES = (
        (HA , 'Habilitar'),
        (DH , 'Deshabilitar'),
        (EL , 'Eliminar'),
        (CR , 'Crear'),
        (ED , 'Editar')
    )

    document = models.ForeignKey(Document)
    user = models.ForeignKey(User)
    modificacion = models.CharField('Modificacion', max_length=12, choices=MODIFICACION_CHOICES)
