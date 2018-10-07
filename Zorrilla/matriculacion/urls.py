from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^form/', formulario, name="form"),
    url(r'^logIn/', logIn, name="logIn"),
    url(r'^login/', login, name="login"),
    url(r'^recuperar/userDocente/', userDocente, name="userDocente"),
    url(r'^get_Secciones/(\d+)/', get_Secciones, name="get_Secciones"),
    url(r'^logout_me_out', logout_me_out, name="logout_me_out"),
    url(r'^pedidos', aceptar_matriculaciones, name="pedidos"),
    url(r'^form_transportista', form_transportista, name="form_transportista"),
    url(r'^todos_los_transportistas/(\d+)/', todos_los_transportistas, name="todos_los_transportistas"),
    url(r'^todos_los_padres/(\d+)/', todos_los_padres, name="todos_los_padres"),
    url(r'^asignar_padre', asignar_padre, name="asignar_padre"),
    url(r'^crear_transportista', crear_transportista, name="crear_transportista"),
    url(r'^asignar_transportista', asignar_transportista, name="asignar_transportista"),
    url(r'^datos_transportista/(\d+)/', datos_transportista, name="datos_transportista"),
    url(r'^cargar_padre/(\d+)/', cargar_padre, name="cargar_padre"),
    url(r'^datos_padre/(\d+)/', datos_padre, name="datos_padre"),
    #url(r'^traer_padres/(\d+)/', traer_padres, name="traer_padres"),
    url(r'crear_alumno', crear_alumno, name="crear_alumno"),
    url(r'crear_padre/(?P<opcion>[\w\-]+)$', crear_padre, name="crear_padre"),
    url(r'^aceptar_matriculacion/$', aceptar_matriculacion, name="aceptar_matriculacion"),
    url(r'^perfilAlumno/(\d+)/$', alumno, name="alumno"),
    url(r'^recuperar/$', template_get_pass, name="template_get_pass")
]
