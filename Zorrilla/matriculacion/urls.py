from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^form/', formulario, name="form"),
    url(r'^formReMatricular/', formReMatricular, name="formReMatricular"),
    url(r'^logIn/', logIn, name="logIn"),
    url(r'^login/', login, name="login"),
    url(r'^aplicar_cambios_alumno/', aplicar_cambios_alumno, name="aplicar_cambios_alumno"),
    url(r'^modificar_curso/(\d+)/', modificar_curso, name="modificar_curso"),
    url(r'^recuperar/user', cambiar_password, name="cambiar_password"),
    url(r'^egresar_alumno', egresar_alumno, name="egresar_alumno"),
    url(r'^get_Secciones/(\d+)/', get_Secciones, name="get_Secciones"),
    url(r'^re_matricular/(\d+)/', re_matricular, name="re_matricular"),
    url(r'^egresar/(\d+)/', egresar, name="egresar"),
    url(r'^logout_me_out', logout_me_out, name="logout_me_out"),
    url(r'^pedidos', traer_pedidos, name="traer_pedidos"),
    url(r'^form_autorizado', form_autorizado, name="form_autorizado"),

    url(r'^aceptar_re_matriculacion', aceptar_re_matriculacion, name="aceptar_re_matriculacion"),
    url(r'^pedido_re_matricular', pedido_re_matricular, name="pedido_re_matricular"),
    url(r'^pedido_egreso', pedido_egreso, name="pedido_egreso"),
    url(r'^crear_obra_social', crear_obra_social, name="crear_obra_social"),
    url(r'^crear_autorizado', crear_autorizado, name="crear_autorizado"),

    url(r'^form_modificar_alumno/(\d+)/', form_modificar_alumno, name="form_modificar_alumno"),
    url(r'^desvincular_transportista', desvincular_transportista, name="desvincular_transportista"),
    url(r'^desvincular_autorizado', desvincular_autorizado, name="desvincular_autorizado"),
    url(r'^desvincular_obra_social', desvincular_obra_social, name="desvincular_obra_social"),
    url(r'^desvincular_familiar', desvincular_familiar, name="desvincular_familiar"),
    url(r'^crear_padre_madre', crear_padre_madre, name="crear_padre_madre"),
    url(r'^cambiar_curso', cambiar_curso, name="cambiar_curso"),
    url(r'^form_transportista', form_transportista, name="form_transportista"),
    url(r'^form_curso', form_curso, name="form_curso"),

    url(r'^form_secretaria_director/(?P<opcion>[\w\-]+)/$', form_secretaria_director, name="form_secretaria_director"),

    url(r'^asignar_autorizado', asignar_autorizado, name="asignar_autorizado"),
    url(r'^crear_curso', crear_curso, name="crear_curso"),
    url(r'^form_obra_social', form_obra_social, name="form_obra_social"),
    url(r'^todos_los_transportistas_asignar/(\d+)/', todos_los_transportistas_asignar, name="todos_los_transportistas_asignar"),
    url(r'^todos_los_padres_asignar/(\d+)/', todos_los_padres_asignar, name="todos_los_padres_asignar"),
    url(r'^todas_las_obras_sociales_asignar/(\d+)/', todas_las_obras_sociales_asignar, name="todas_las_obras_sociales_asignar"),
    url(r'^asignar_padre', asignar_padre, name="asignar_padre"),
    url(r'^asignar_obra_social', asignar_obra_social, name="asignar_obra_social"),

    url(r'^crear_trabajador', crear_trabajador, name="crear_trabajador"),

    url(r'^todas_las_obras_sociales', todas_las_obras_sociales, name="todas_las_obras_sociales"),
    url(r'^crear_transportista', crear_transportista, name="crear_transportista"),
    url(r'^asignar_transportista', asignar_transportista, name="asignar_transportista"),
    url(r'^datos_transportista/(\d+)/', datos_transportista, name="datos_transportista"),
    url(r'^cargar_padre/(\d+)/', cargar_padre, name="cargar_padre"),
    url(r'^datos_padre/(\d+)/', datos_padre, name="datos_padre"),
    url(r'^datos_autorizado/(\d+)/', datos_autorizado, name="datos_autorizado"),
    url(r'^datos_obra_social/(?P<id_obra_social>\d+)/', datos_obra_social, name="datos_obra_social"),
    url(r'^padres_del_alumno/(\d+)/', padres_del_alumno, name="padres_del_alumno"),
    url(r'^usuarios_transportista/(\d+)/', usuarios_transportista, name="usuarios_transportista"),
    url(r'^transportistas_del_alumno/(\d+)/', transportistas_del_alumno, name="transportistas_del_alumno"),
    url(r'^autorizados_del_alumno/(\d+)/', autorizados_del_alumno, name="autorizados_del_alumno"),
    url(r'^obras_sociales_del_alumno/(\d+)/', obras_sociales_del_alumno, name="obras_sociales_del_alumno"),
    url(r'^todos_los_autorizados_asignar/(\d+)/', todos_los_autorizados_asignar, name="todos_los_autorizados_asignar"),
    url(r'crear_alumno', crear_alumno, name="crear_alumno"),
    url(r'crear_padre/$', crear_padre, name="crear_padre"),
    url(r'^aceptar_matriculacion/$', aceptar_matriculacion, name="aceptar_matriculacion"),
    url(r'^perfilAlumno/(?P<opcion>[\w\-]+)-(?P<dni_alumno>\d+)$', datos_alumno, name="datos_alumno"),
    url(r'^todos_los_transportistas/$', todas_los_transportistas, name="todas_los_transportistas"),
    url(r'^recuperar/$', template_get_pass, name="template_get_pass")
]
