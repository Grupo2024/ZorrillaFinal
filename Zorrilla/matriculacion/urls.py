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
    url(r'^recuperar/user', cambiar_password, name="cambiar_password"),
    url(r'^get_Secciones/(\d+)/', get_Secciones, name="get_Secciones"),
    url(r'^re_matricular/(\d+)/', re_matricular, name="re_matricular"),
    url(r'^logout_me_out', logout_me_out, name="logout_me_out"),
    url(r'^pedidos', traer_pedidos, name="traer_pedidos"),
    url(r'^form_transportista', form_transportista, name="form_transportista"),
    url(r'^todos_los_transportistas/(\d+)/', todos_los_transportistas, name="todos_los_transportistas"),
    url(r'^todos_los_padres/(\d+)/', todos_los_padres, name="todos_los_padres"),
    url(r'^asignar_padre', asignar_padre, name="asignar_padre"),
    url(r'^crear_transportista', crear_transportista, name="crear_transportista"),
    url(r'^asignar_transportista', asignar_transportista, name="asignar_transportista"),
    url(r'^datos_transportista/(\d+)/', datos_transportista, name="datos_transportista"),
    url(r'^cargar_padre/(\d+)/', cargar_padre, name="cargar_padre"),
    url(r'^datos_padre/(\d+)/', datos_padre, name="datos_padre"),
    url(r'^padres_del_alumno/(\d+)/', padres_del_alumno, name="padres_del_alumno"),
    url(r'^transportistas_del_alumno/(\d+)/', transportistas_del_alumno, name="transportistas_del_alumno"),
    url(r'^obras_sociales_del_alumno/(\d+)/', obras_sociales_del_alumno, name="obras_sociales_del_alumno"),
    url(r'crear_alumno', crear_alumno, name="crear_alumno"),
    url(r'crear_padre/(?P<opcion>[\w\-]+)$', crear_padre, name="crear_padre"),
    url(r'^aceptar_matriculacion/$', aceptar_matriculacion, name="aceptar_matriculacion"),
    url(r'^perfilAlumno/(\d+)/$', datos_alumno, name="datos_alumno"),
    url(r'^recuperar/$', template_get_pass, name="template_get_pass")
]
