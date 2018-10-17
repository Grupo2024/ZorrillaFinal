# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

admin.site.register(Profesor)
admin.site.register(Director)
admin.site.register(Secretaria)
admin.site.register(Curso)
admin.site.register(clave_Docente)
admin.site.register(user_Docente)
admin.site.register(user_Secretaria)
admin.site.register(user_Director)
# Register your models here.
