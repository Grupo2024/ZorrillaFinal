from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^form', formulario, name="form"),
    url(r'^cursos', cursos, name="cursos"),
    url(r'^logIn', logIn, name="logIn"),
    url(r'^pedidos', aceptar_matriculaciones, name="aceptar_matriculaciones"),
    url(r'crear_alumno/', crear_alumno, name="crear_alumno"),
    url(r'^aceptar_matriculacion/(?P<id_matriculacion>\d+)$', aceptar_matriculacion, name="aceptar_matriculacion"),
]