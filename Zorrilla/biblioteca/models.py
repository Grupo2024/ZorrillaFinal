# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Document(models.Model):


    DR = 'Drama'
    RO = 'Romance'
    AC = 'Accion'
    CF = 'Ciencia Ficcion'
    TR = 'Terror'
    AV = 'Aventura'
    PO = 'Policial'
    PL = 'Politica'
    FA = 'Fantasia'
    OT = 'Otros'

    GENERO_CHOICES = (
        (DR , 'Drama'),
        (RO , 'Romance'),
        (AC , 'Accion'),
        (CF , 'Ciencia Ficcion'),
        (TR , 'Terror'),
        (AV , 'Aventura'),
        (PO , 'Policial'),
        (PL , 'Politica'),
        (FA , 'Fantasia'),
        (OT , 'Otros')
    )

    description = models.CharField(max_length=255, null=False)
    document = models.FileField(upload_to='')
    title = models.CharField(max_length=60, blank=False, null=False)
    genero = models.CharField('Modificacion', max_length=15, choices=GENERO_CHOICES)
    autor = models.CharField(max_length=60, blank=False, null=False)
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

    def reverse(self):
        if self.habilitado:
            return "Deshabilitado"
        else:
            return "Habilitado"
        
    def cantidad_habilitados():
        return Document.objects.filter(habilitado=True).count()
    
    def cantidad_deshabilitados():
        return Document.objects.filter(habilitado=False).count()
    
        
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
    uploaded_at = models.DateTimeField(auto_now_add=True)
