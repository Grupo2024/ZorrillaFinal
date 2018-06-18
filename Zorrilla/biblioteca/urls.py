from django.conf.urls import url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^biblioteca', biblioteca, name="biblioteca"),
    url(r'^filter_books/', filter_books, name="filter_books"),
    url(r'^eliminar_libro/(?P<id_documento>\d+)$', eliminar_libro, name="eliminar_libro"),
    url(r'^info_libro/(?P<id_documento>\d+)$', info_libro, name="info_libro"),
    url(r'^filtered_books/(?P<attribute>[\w\-]+)-(?P<cantidad>\d+)$', filtered_books, name="filtered_books"),
    url(r'^cargado/', cargado, name="cargado"),
    url(r'^all_the_books/', all_the_books, name="all_the_books")
    
]
