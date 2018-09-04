# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .forms import DocumentForm
from django.http import JsonResponse
import datetime
from .decorators import *
import xlwt

@user_passes_test(check_Secretaria)
def estadisticas(request):
    libros_habilitados = Document.objects.filter(habilitado=True).count()
    libros_deshabilitados = Document.objects.filter(habilitado=False).count()
    cant_drama = Document.objects.filter(genero="Drama").count()
    cant_romance = Document.objects.filter(genero="Romance").count()
    cant_accion = Document.objects.filter(genero="Accion").count()
    cant_cf = Document.objects.filter(genero="Ciencia Ficcion").count()
    cant_terror = Document.objects.filter(genero="Terror").count()
    cant_aventura = Document.objects.filter(genero="Aventura").count()
    cant_policial = Document.objects.filter(genero="Policial").count()
    cant_politica = Document.objects.filter(genero="Politica").count()
    cant_fantasia = Document.objects.filter(genero="Fantasia").count()
    cant_otros = Document.objects.filter(genero="Otros").count()
    """
    DR = 'Drama'
    RO = 'Romance'
    AC = 'Accion'
    CF = 'Ciencia Ficcion'
    TR = 'Terror'
    AV = 'Aventura'
    PO = 'Policial'
    PL = 'Politica'
    FA = 'Fantasia'
    OT = 'Otros'
    """

    data = {
        'libros_habilitados': libros_habilitados,
        'libros_deshabilitados': libros_deshabilitados,
        'cant_drama':cant_drama,
        'cant_romance':cant_romance,
        'cant_accion':cant_accion,
        'cant_cf':cant_cf,
        'cant_terror':cant_terror,
        'cant_aventura':cant_aventura,
        'cant_policial':cant_policial,
        'cant_politica':cant_politica,
        'cant_fantasia':cant_fantasia,
        'cant_otros':cant_otros
    }
    return render (request, 'estadisticas.html', {'datos_libros':data})

@user_passes_test(check_Director)
def export_books(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reporte_biblioteca.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Books')

    # Sheet header, first row
    row_num = 3

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id','Titulo', 'Autor', 'Genero', 'Habilitado']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
        
    rows = Document.objects.all().order_by('title','estado').values_list('id','title', 'autor', 'genero', 'habilitado')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

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

@user_passes_test(check_Director)
def informe(request):
    documents = Document.objects.all()
    documents_habiltiados = Document.objects.filter(habilitado=True).count()
    documents_deshabiltiados = Document.objects.filter(habilitado=False).count()
    documentos = {
        'cantidad':documents.count(),
        'habilitados':documents_habiltiados,
        'deshabilitados':documents_deshabiltiados
    }
    return render(request, 'informe.html', {'documentos':documentos})
    
@user_passes_test(check_Director)
def historia_libro(request, id_documento):
    if request.method == 'POST':
        estados = Estado.objects.filter(document__id=id_documento).order_by('id')
        return render(request, 'estados.html', {'estados':estados})

@user_passes_test(check_Director)
def libros_habilitados(request, cantidad):
    documents = Document.objects.filter(habilitado=False).order_by('-title')[:cantidad]
    form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})
    
    
@login_required
def cargado(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            document = form.cleaned_data['document']
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
            print "No es valido"
            data = {
                'estado': "Hubo un error " ,
                'error': True
            }
    return JsonResponse(data)
    
# Function that changes the document habilitado attribute to False, it does not delete the book,
@user_passes_test(check_Director_or_Profesor)
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

@user_passes_test(check_Director)
def cambiar_estado_libro(request, id_documento):
    document = Document.objects.get(id=id_documento)
    estado = Estado(document=document, user=request.user, modificacion=document.reverse())
    document.change()
    document.save()
    estado.save()
    aux = "Deshabilitado"
    if document.habilitado:
        aux = "Habilitado"
    data = {
        'estado':'El libro ' + str(document.title) + " ha cambiado su estado a " + str(aux)
    }
    return JsonResponse(data, safe=True)


def info_libro(request, id_documento):
    if request.method == 'POST':
        document = Document.objects.get(id=id_documento)
        return render(request, 'book_info.html', {'doc':document})

def all_the_books(request):
    documents = Document.objects.filter(habilitado=True)
    form = DocumentForm()
    return render (request, 'biblioteca.html', {'documentos':documents, 'form':form})

def filtered_books(request, attribute, cantidad):
    print attribute
    print cantidad
    documents = Document.objects.filter(habilitado=True).order_by('-' + str(attribute))[:cantidad]
    form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})
