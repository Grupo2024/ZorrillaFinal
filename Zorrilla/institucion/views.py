# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.
def perfil_profesor(request):
    return render(request, 'templates_docentes/perfil_profesor.html')

def cursos1(request):
    return render(request, 'templates_cursos/cursos1.html')

def cursos2(request, turno):
    print turno
    if turno == 'Maniana':
        turno = False
    else:
        turno = True
    grados = Grado.objects.filter(turno_asignado__hora=turno)
    return render(request, 'templates_cursos/cursos2.html', {'todos_los_grados':grados})

def cursos3(request):
    return render(request, 'templates_cursos/cursos3.html')

def cursos4(request):
    return render(request, 'templates_cursos/cursos4.html')

def docentes(request):
    return render(request, 'templates_docentes/docentes.html')
