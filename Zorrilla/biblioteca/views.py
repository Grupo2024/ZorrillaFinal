# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from .forms import DocumentForm
from django.http import JsonResponse

def filter_books(request):
    return render(request, 'filter_books.html')

def biblioteca(request):
    documents = Document.objects.filter(habilitado=True).order_by('?')[:5]
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #aux = request.POST['id_form']
            form.save()
            #document = Document.objects.get(document_id=aux)
            #estado = Estado(document = form, user=request.user, modificacion="Crear")
            #estado.save()

            return redirect ('biblioteca')

    else:
        form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})


# Function that changes the document habilitado attribute to False, it does not delete the book,
# only Directora can do it.

#Decorator missing.
def eliminar_libro(request, id_documento):
    document = Document.objects.get(id=id_documento)
    #estado = Estado(document=document, user=request.user, modificacion="Deshabilitar")
    document.habilitado = False
    document.save()
    #estado.save()
    data = {
        'estado': "El libro " + str(document.title) + " ha sido eliminado"
    }
    return JsonResponse(data, safe=True)
