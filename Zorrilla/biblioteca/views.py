# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from .forms import DocumentForm

def filter_books(request):
    return render(request, 'filter_books.html')

def biblioteca(request):
    documents = Document.objects.all().order_by('?')[:2]
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        description=request.POST['description']
        document=request.FILES['document']
        title=request.POST['title']
        tipo=request.POST['tipo']
        autor=request.POST['autor']
        editorial=request.POST['editorial']
        fecha_lanzamiento=request.POST['fecha_lanzamiento']
        cantidad_paginas=request.POST['cantidad_paginas']
        genero=request.POST['genero']
        habilitado=request.POST['habilitado']
        if habilitado == 'on':
            habilitado = True
        else:
            habilitado = False
        document = Document (description=description, document=document, title=title, tipo=tipo,
        autor=autor,editorial=editorial, fecha_lanzamiento=fecha_lanzamiento, cantidad_paginas=cantidad_paginas
        , genero=genero, habilitado=habilitado)

        document.save()

        print document.document.name

        estado = Estado(document=document, user=request.user, modificacion="Crear")
        estado.save()
        return redirect ('biblioteca')

    else:
        form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})
