from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^biblioteca', biblioteca, name="biblioteca"),
    url(r'^eliminar_libro/$', eliminar_libro, name="eliminar_libro"),
    url(r'^cambiar_estado_libro/$', cambiar_estado_libro, name="cambiar_estado_libro"),
    url(r'^info_libro/(?P<id_documento>\d+)$', info_libro, name="info_libro"),
    url(r'^historia_libro/(?P<id_documento>\d+)$', historia_libro, name="historia_libro"),
    url(r'^filtered_books/$', filtered_books, name="filtered_books"),
    url(r'^libros_deshabilitados/(?P<cantidad>\d+)$', libros_deshabilitados, name="libros_deshabilitados"),
    url(r'^cargado/', cargado, name="cargado"),
    url(r'^informe/', informe, name="informe"),
    url(r'^estadisticas/',estadisticas, name="estadisticas"),
    url(r'^export/xls/$', export_books, name='export_books'),
    url(r'^all_the_books/', all_the_books, name="all_the_books")
]
