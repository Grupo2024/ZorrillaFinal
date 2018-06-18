
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from .forms import DocumentForm
from django.http import JsonResponse
import os

def filter_books(request):
    return render(request, 'filter_books.html')

def biblioteca(request):
    documents = Document.objects.filter(habilitado=False).order_by('-uploaded_at')[:5]
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = DocumentForm()
            return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})

    else:
        form = DocumentForm()
        data = "Hola"
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form, 'data':data})

def cargado(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.cleaned_data['document']
            title = form.cleaned_data['title']
            error = False
            print document
            print title
            aux = Document.objects.filter(title=title)
            if aux:
                resultado = "Ya existe un Archivo con ese titulo"
                error = True
            aux = Document.objects.filter(document=document)
            if aux:
                resultado = "Ya existe un Archivo con ese nombre"
                error = True
            if error:
                data = {
                    'estado': resultado,
                    'error': True
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
        data = {
            'estado': "Fallo"
        }
        return JsonResponse(data)
    
# Function that changes the document habilitado attribute to False, it does not delete the book,
# only Directora can do it.

#Decorator missing.
def eliminar_libro(request, id_documento):
    document = Document.objects.get(id=id_documento)
    estado = Estado(document=document, user=request.user, modificacion="Deshabilitar")
    document.change()
    document.save()
    estado.save()
    """
    rout = "../media/" + str(document.document)
    os.remove(rout)
    """   
    data = {
        'estado': "El libro " + str(document.title) + " ha sido eliminado"
    }
    return JsonResponse(data, safe=True)

def info_libro(request, id_documento):
    document = Document.objects.get(id=id_documento)
    return render(request, 'book_info.html', {'doc':document})
