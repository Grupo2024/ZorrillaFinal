# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Archivo(models.Model):
    fecha = models.DateTimeField('Fecha en la que se subio el archivo', null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    descripcion = models.CharField('Descripcion del archivo que se esta subiendo')

