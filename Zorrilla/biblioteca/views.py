
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .forms import DocumentForm
from django.http import JsonResponse
import datetime
from .decorators import *


def filter_books(request):
    return render(request, 'filter_books.html')

def biblioteca(request):
    documents = Document.objects.filter(habilitado=True).order_by('-uploaded_at')[:5]
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = DocumentForm()
            return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})

    else:
        form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})

def cargado(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            autor = form.cleaned_data['autor']
            tipo = form.cleaned_data['tipo']
            title = form.cleaned_data['title']
            document = form.cleaned_data['document']
            fecha = form.cleaned_data['fecha_lanzamiento']
            error = False
            aux = Document.objects.filter(title=title)
            if aux:
                resultado = "Ya existe un registro con ese Titulo"
                error = True
            aux = Document.objects.filter(document=document)
            if aux:
                resultado = "Ese archivo ya fue cargado"
                error = True
            if error:
                data = {
                    'estado': resultado,
                    'error': error
                }
            else:
                form.save()
                document = Document.objects.get(title=title)
                estado = Estado(document = document, user=request.user, modificacion="Crear")
                estado.save()
                data = {
                    'estado': "El libro " + str(document) + " ha sido cargado",
                    'error': False
                }
        else:
            cantidad_paginas = form.data['cantidad_paginas']
            fecha_lanzamiento = form.data['fecha_lanzamiento']
            mistake= ""
            if type(fecha_lanzamiento) is not datetime.date:
                mistake = "Fecha tiene el formato, Ej: 2010-12-31"
            fallo = ""
            try:
                value = int(cantidad_paginas)
            except ValueError:
                fallo = "Cantidad de Paginas es con numeros "
            print "No es valido"
            data = {
                'estado': str(mistake) + " " + str(fallo),
                'error': True
            }
    return JsonResponse(data)
    
# Function that changes the document habilitado attribute to False, it does not delete the book,
# only Directora can do it.

def eliminar_libro(request, id_documento):
    document = Document.objects.get(id=id_documento)
    estado = Estado(document=document, user=request.user, modificacion="Deshabilitar")
    document.change()
    document.save()
    estado.save()
    if request.user.groups.filter(name="Director").exists():   
        document.delete()
        print "es director"
        data = {
            'estado': "El libro " + str(document.title) + " y todos los registros del mismo han sido eliminados"
        }
    else:
        data = {
            'estado': "El libro " + str(document.title) + "  ha sido eliminado"
        }
    return JsonResponse(data, safe=True)

def info_libro(request, id_documento):
    if request.method == 'POST':
        document = Document.objects.get(id=id_documento)
        return render(request, 'book_info.html', {'doc':document})

def all_the_books(request):
    documents = Document.objects.all()
    form = DocumentForm()
    return render (request, 'biblioteca.html', {'documentos':documents, 'form':form})

def filtered_books(request, attribute, cantidad):
    print attribute
    print cantidad
    documents = Document.objects.filter(habilitado=True).order_by('-' + str(attribute))[:cantidad]
    form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})
    