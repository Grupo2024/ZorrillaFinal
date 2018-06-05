from django.shortcuts import render
from .models import *
from .creation import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')

def cursos(request):
    return render(request, 'cursos.html')

def aceptar_matriculaciones(request):
    print request.user
    alumnos = Alumno.objects.all()
    print alumnos
    matriculaciones = Matriculacion.objects.all().order_by('-fecha_matriculacion')
    print matriculaciones
    return render(request, 'pedidos.html', {'matriculaciones':matriculaciones})