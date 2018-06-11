# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from .forms import DocumentForm

def filter_books(request):
    return render(request, 'filter_books.html')

def biblioteca(request):
    documents = Document.objects.all().order_by('?')[:5]
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ('biblioteca')

    else:
        form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})
