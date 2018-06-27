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
# Register your models here.
