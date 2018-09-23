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
    HA = 'Habilitado'
    DE = 'Deshabilitado'

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

    HABILITADO_CHOICES = (
        (HA, 'Habilitado'),
        (DE , 'Deshabilitado')
    )

    description = models.CharField(max_length=255, null=False)
    document = models.FileField(upload_to='', unique=True)
    title = models.CharField(max_length=60, blank=False, null=False, unique=True)
    genero = models.CharField('Genero', max_length=15, choices=GENERO_CHOICES)
    autor = models.CharField(max_length=60, blank=False, null=False)
    habilitado = models.CharField('Habilitado', max_length=13, choices=HABILITADO_CHOICES, default=HABILITADO_CHOICES[0][0])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Titulo {}, id {}'.format(self.title, self.id)

    def cantidad_habilitados(self):
        return Document.objects.filter(habilitado="Habilitado").count()
    
    def cantidad_deshabilitados(self):
        return Document.objects.filter(habilitado="Deshabilitado").count()
    
        
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


    def __str__(self):
        return '{} {}'.format(self.modificacion, self.document.title)
