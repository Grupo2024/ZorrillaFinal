"""Zorrilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from matriculacion .views import *
from institucion .views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #Url for Templates

    url(r'^$', index, name="index"),
    url(r'^form', formulario, name="form"),
    url(r'^cursos', cursos, name="cursos"),

    url(r'^turnos', cursos1, name="cursos1"),
    url(r'^grados', cursos2, name="cursos2"),
    url(r'^seccion', cursos3, name="cursos3"),
    url(r'^alumnos', cursos4, name="cursos4"),

    url(r'^docentes_lista',docentes_lista, name="docentes_lista"),

    url(r'^perfil_profesor', perfil_profesor, name="perfil_profesor"),
    url(r'^pedidos', aceptar_matriculaciones, name="aceptar_matriculaciones"),

    #Url for models creation

    url(r'crear_alumno/', crear_alumno, name="crear_alumno")
]
