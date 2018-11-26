from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #Url sin parametros

    url(r'^docentes',docentes, name="docentes"),
    url(r'^mi_perfil',mi_perfil, name="mi_perfil"),
    url(r'^template_email_docente',template_email_docente, name="template_email_docente"),
    url(r'^email_for_logIn',email_for_logIn, name="email_for_logIn"),
    url(r'^modificar_datos_perfil',modificar_datos_perfil, name="modificar_datos_perfil"),
    url(r'^turnos', cursos1, name="cursos1"),
    url(r'crear_profesor/', crear_profesor, name="crear_profesor"),
    url(r'^formProfesor', formProfesor, name="formProfesor"),

    #Url con ID


    url(r'^seccion/(?P<id_curso>\d+)$', cursos3, name="cursos3"),
    url(r'^datos_alumno/(?P<dni_alumno>\d+)$', datos_alumno, name="datos_alumno"),
    url(r'^volver_curso/(?P<dni_alumno>\d+)$', volver_curso, name="volver_curso"),
    url(r'^perfilProfesor/(\d+)/$', profesor, name="profesor"),
    url(r'modificar_perfil/(?P<dni>\d+)/$', modificar_perfil, name="modificar_perfil"),

    #Url con String

    url(r'^grados/(?P<turno>[\w\-]+)$', cursos2, name="cursos2"),

    #Url ID y String

    url(r'^get_alumno/(?P<string>[\w\-]+)-(?P<dni_alumno>\d+)$', get_alumno, name="get_alumno"),



]
