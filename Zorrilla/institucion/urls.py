from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^turnos', cursos1, name="cursos1"),
    url(r'^grados', cursos2, name="cursos2"),
    url(r'^seccion', cursos3, name="cursos3"),
    url(r'^alumnos', cursos4, name="cursos4"),
    url(r'^docentes',docentes, name="docentes"),
    url(r'^perfilProfesor/(\d+)/$', profesor, name="profesor"),
    url(r'^dlt_profesor/(\d+)/$', eliminar_docente, name="eliminar_docente"),
    url(r'^logged', login, name="login"),
]