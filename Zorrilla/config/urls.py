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
from biblioteca .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #Url for Templates

    url(r'^$', index, name="index"),
    url(r'^form', formulario, name="form"),
    url(r'^pedidos', solicitar_matriculacion, name="solicitar_matriculacion"),
    url(r'^biblioteca', biblioteca, name="biblioteca"),
    url(r'filter_books/', filter_books, name="filter_books"),

    #Url for models creation

    url(r'crear_alumno/', crear_alumno, name="crear_alumno"),

    #url for an ID

    url(r'^aceptar_matriculacion/(?P<id_matriculacion>\d+)$', aceptar_matriculacion, name="aceptar_matriculacion"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
