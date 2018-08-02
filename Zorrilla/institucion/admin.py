# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Profesor)
admin.site.register(Director)
admin.site.register(Secretaria)
admin.site.register(Turno)
admin.site.register(Seccion)
admin.site.register(Grado)
admin.site.register(clave_Docente)
admin.site.register(Asignacion)
admin.site.register(user_Docente)
admin.site.register(user_Secretaria)
# Register your models here.
