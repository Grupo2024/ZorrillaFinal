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

@user_passes_test(check_Director_or_Secretaria)
def estadisticas(request):
    libros_habilitados = Documento.objects.filter(habilitado="Habilitado").count()
    libros_deshabilitados = Documento.objects.filter(habilitado="Deshabilitado").count()
    cant_drama = Documento.objects.filter(genero="Drama").count()
    cant_romance = Documento.objects.filter(genero="Romance").count()
    cant_accion = Documento.objects.filter(genero="Accion").count()
    cant_cf = Documento.objects.filter(genero="Ciencia Ficcion").count()
    cant_terror = Documento.objects.filter(genero="Terror").count()
    cant_aventura = Documento.objects.filter(genero="Aventura").count()
    cant_policial = Documento.objects.filter(genero="Policial").count()
    cant_politica = Documento.objects.filter(genero="Politica").count()
    cant_fantasia = Documento.objects.filter(genero="Fantasia").count()
    cant_otros = Documento.objects.filter(genero="Otros").count()
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

@user_passes_test(check_Secretaria)
def export_books(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reporte_biblioteca.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Books')

    # Sheet header, first row
    row_num = 3

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Titulo', 'Autor', 'Genero','Habilitado']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining filas
    font_style = xlwt.XFStyle()

    filas = Documento.objects.all().order_by('titulo').values_list('titulo', 'autor', 'genero','habilitado').distinct()
    print (filas)
    for row in filas:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def biblioteca(request):
    documents = Documento.objects.filter(habilitado="Habilitado").order_by('-fecha', 'titulo')[:5]
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = DocumentForm()
            return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})
    else:
        form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})

@user_passes_test(check_Secretaria)
def informe(request):
    documents = Documento.objects.all()
    documents_habiltiados = Documento.objects.filter(habilitado="Habilitado").count()
    documents_deshabiltiados = Documento.objects.filter(habilitado="Deshabilitado").count()
    print (documents_habiltiados)
    documentos = {
        'cantidad':documents.count(),
        'habilitados':documents_habiltiados,
        'deshabilitados':documents_deshabiltiados
    }
    return render(request, 'informe.html', {'documentos':documentos})
    
@user_passes_test(check_Secretaria)
def historia_libro(request, id_documento):
    if request.method == 'POST':
        estados = Estado.objects.filter(document__id=id_documento).order_by('id')
        return render(request, 'estados.html', {'estados':estados})

@user_passes_test(check_Secretaria)
def libros_deshabilitados(request, cantidad):
    documents = Documento.objects.filter(habilitado="Deshabilitado").order_by('-titulo')[:cantidad]
    form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})
    
    
@login_required
def cargado(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['titulo']
            document = Documento.objects.get(titulo=title)
            estado = Estado(document = document, user=request.user, modificacion="Crear")
            estado.save()
            data = {
                'estado': "El libro " + str(document) + " ha sido cargado",
                'error': False
            }
        else:
            print ("No es valido")
            data = {
                'estado': str(form.errors),
                'error': True
            }
    return JsonResponse(data)

@user_passes_test(check_Profesor_or_Secretaria)
def eliminar_libro(request, id_documento):
    document = Documento.objects.get(id=id_documento)
    estado = Estado(document=document, user=request.user, modificacion="Deshabilitar")
    document.habilitado = "Deshabilitado"
    document.save()
    estado.save()
    data = {
        'estado':" El libro " + str(document.titulo) + " ha sido Deshabilitado."
    }
    return JsonResponse(data, safe=True)

@user_passes_test(check_Secretaria)
def cambiar_estado_libro(request, id_documento):
    new_document = Documento.objects.get(id=id_documento)
    print (new_document.habilitado)
    aux = "Deshabilitado"
    if new_document.habilitado == "Habilitado":
        new_document.habilitado="Deshabilitado"
        new_document.save()
    else:
        aux="Habilitado"
        new_document.habilitado="Habilitado"
        new_document.save()
    estado = Estado(document=new_document, user=request.user, modificacion=aux)
    estado.save()
    data = {
        'estado':'El libro ' + str(new_document.titulo) + " ha cambiado su estado a " + str(new_document.habilitado)
    }
    return JsonResponse(data, safe=True)


def info_libro(request, id_documento):
    document = Documento.objects.get(id=id_documento)
    return render(request, 'book_info.html', {'doc':document})

def all_the_books(request):
    documents = Documento.objects.filter(habilitado="Habilitado")
    form = DocumentForm()
    return render (request, 'biblioteca.html', {'documentos':documents, 'form':form})

def filtered_books(request):
    cantidad = request.POST['cantidad']
    print (cantidad)
    genero = request.POST['ordenar_por']
    print (genero)
    sentido = request.POST['sentido']
    print (sentido)
    habilitado = request.POST['habilitado_libros']
    print (habilitado)
    if (sentido == "+"):
        sentido = ""
    documents = Documento.objects.filter(habilitado=habilitado).order_by(str(sentido) + str(genero))[:cantidad]
    form = DocumentForm()
    return render(request, 'biblioteca.html', {'documentos':documents, 'form':form})
