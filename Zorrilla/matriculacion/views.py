# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from biblioteca.decorators import *
from institucion.forms import *
import xlwt
import datetime

# Create your views here.

def daddy():
    cant_profesores = Trabajador.objects.all().count()
    if cant_profesores == 0:
        password = "hola1234"
        user_secretaria = User.objects.create_user(username="secretaria", password=password)
        grupo_secretaria, created = Group.objects.get_or_create(name='Secretaria')
        user_profesor = User.objects.create_user(username="profesor", password=password)
        grupo_profesor, created = Group.objects.get_or_create(name='Profesor')
        user_director = User.objects.create_user(username="director", password=password)
        grupo_director, created = Group.objects.get_or_create(name='Director')
        grupo_admin, created = Group.objects.get_or_create(name='Admin_Secretaria')
        grupo_secretaria = Group.objects.get(name='Secretaria') 
        user_admin = User.objects.create_user(username="admin_s", password=password)
        grupo_secretaria.user_set.add(user_secretaria)
        my_group2 = Group.objects.get(name='Profesor') 
        my_group2.user_set.add(user_profesor)
        my_group3 = Group.objects.get(name='Director') 
        my_group3.user_set.add(user_director)
        grupo_admin = Group.objects.get(name='Admin_Secretaria')
        grupo_admin.user_set.add(user_admin)
        #new_group, created = Group.objects.get_or_create(name='new_group')
        a = Trabajador(nombre_t="a", apellido_t="a", dni_t=11111111, lugar_nacimiento_t="a",
        fecha_nacimiento_t="1980-01-01", domicilio_t="a", email_t="mumi@gmail.com", sexo_t="Mujer",cargo_t="SE",
        telefono_particular=1, telefono_laboral=1, telefono_familiar=1, datos_familiares_cargo="a",
        fecha_inicio_actividad="2018-03-01", antecedentes_laborales="a", estudios_cursados="a") 
        b = Trabajador(nombre_t="b", apellido_t="b", dni_t=22222222, lugar_nacimiento_t="b",
        fecha_nacimiento_t="1980-02-02", domicilio_t="b", email_t="pancho@gmail.com", sexo_t="Hombre", cargo_t="PR",
        telefono_particular=2, telefono_laboral=2, telefono_familiar=2, datos_familiares_cargo="b",
        fecha_inicio_actividad="2018-02-02", antecedentes_laborales="b", estudios_cursados="b")
        c = Trabajador(nombre_t="c", apellido_t="c", dni_t=33333333, lugar_nacimiento_t="c",
        fecha_nacimiento_t="1980-03-03", domicilio_t="c", email_t="arce@gmail.com", sexo_t="dudoso",cargo_t="DI",
        telefono_particular=3, telefono_laboral=3, telefono_familiar=3, datos_familiares_cargo="c",
        fecha_inicio_actividad="2018-03-03", antecedentes_laborales="c", estudios_cursados="c")
        a.save()
        b.save()
        c.save()
        secretaria_aux = user_Trabajador(user=user_secretaria,trabajador=a)
        profesor_aux = user_Trabajador(user=user_profesor,trabajador=b)
        director_aux = user_Trabajador(user=user_director,trabajador=c)
        secretaria_aux.save()
        profesor_aux.save()
        director_aux.save()
        datos_index = datos_Index(telefono=1234567, telefono2=1234567, email="robert@gmail.com", email2="pipo@gmail.com",
        latitud=123123, longitud=789456)
        datos_index.save()
        return "Creados"
    else:
        return "Ya estan creados"

"""
===================
Levantar Templates.
===================
"""

def asdf(request):
    return render(request, 'responsive.html')

def logIn(request):
    return render(request, 'docentes_login.html')

def index(request):
    daddy()
    datos = datos_Index.objects.get(pk=1)
    return render(request, 'index.html', {'datos':datos})

@login_required
def logout_me_out(request):
    auth.logout(request)
    return redirect ('index')

@user_passes_test(check_Secretaria)
def form_egresados(request):
    return render(request, 'templates_cursos/egresar_file.html')

@user_passes_test(check_Secretaria)
def generar_egreso(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reporte_egresados.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Books')

    # Sheet header, first row
    row_num = 3

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nombre', 'Apellido', 'Dni']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining filas
    font_style = xlwt.XFStyle()

    filas = Matriculacion.objects.filter(matriculado="Eg").order_by('fecha_matriculacion').values_list('alumno__nombre', 'alumno__apellido', 'alumno__dni').distinct()
    print (filas)
    for row in filas:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

"""
==============================¿
Pasar ModelForm a un Template.
==============================
"""

#Levantar Template para cargar Alumno y Padre del mismo.
def formulario(request):
    alumno_form = AlumnoForm()
    padre_form = PadreForm()
    return render(request, 'formulario.html', {'alumno_form':alumno_form, 'padre_form':padre_form})

#Levantar Template para cargar un pedido de Rematriculacion.
def formReMatricular(request):
    re_matricular_form = ReMatricularForm()
    return render(request, 'Re_matricular/form_re_matricular.html', {'re_matricular_form':re_matricular_form})

#Levantar Template para cargar Transportista.
def form_transportista(request):
    form_transportista = TransportistaForm()
    objetivo = "Crear"
    return render (request, 'Transportista/crear_transportista.html', {'form_transportista':form_transportista, 'objetivo':objetivo})

#Levantar el Form para cambiar la password.
def template_get_pass(request):
    print ("entra")
    form = get_Password()
    return render (request, 'new_password/my_info.html', {'form':form})

#Levantar el Form para cargar al Padre.
def cargar_padre(request, dni_alumno):
    padre_form = PadreForm()
    objetivo = "Cargar"
    return render(request, 'Padre_madre/crear_padre_madre.html', {'padre_form':padre_form, 'dni_alumno':dni_alumno, 'objetivo':objetivo})

def form_autorizado(request):
    opcion = "Crear"
    autorizado = AutorizadoForm(initial={'fecha_nacimiento':'dia/mes/año'})
    return render(request, 'Autorizado/crear_autorizado.html', {'autorizado':autorizado, 'opcion':opcion})

def form_secretaria_director(request, opcion):
    form = ProfesorForm()
    cargo_titulo = "Secretaria"
    if (opcion=="DI"):
        cargo_titulo = "Director"
    return render (request, 'Admin_Secretaria/form_secretaria_director.html', {'form':form, 'cargo':opcion, 'cargo_titulo':cargo_titulo})

#Levantar el Form para cargar una Obra Social.
def form_obra_social(request):
    obra_social = Obra_SocialForm()
    return render(request, 'Obra_Social/crear_obra_social.html', {'obra_social':obra_social})

#Levantar el Form para cargar un Curso.
def form_curso(request):
    return render(request, 'templates_cursos/crear_curso.html')

@user_passes_test(check_Secretaria)
def form_modificar_alumno(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    alumno_form = Modificar_Alumno_Form(initial={'nombre':alumno.nombre.title(), 'apellido':alumno.apellido.title(),'lugar_nacimiento':alumno.lugar_nacimiento.title(), 'fecha_nacimiento':alumno.fecha_nacimiento, 'domicilio':alumno.domicilio.title(), 'email':alumno.email, 'sexo':alumno.sexo, 'telefono_casa':alumno.telefono_casa, 'telefono_padre':alumno.telefono_padre, 'telefono_madre':alumno.telefono_madre, 'telefono_familiar':alumno.telefono_familiar, 'telefono_vecino':alumno.telefono_vecino, 'enfermedad_relevante':alumno.enfermedad_relevante.title(), 'con_quien_vive':alumno.con_quien_vive.title(), 'quien_lo_trae':alumno.quien_lo_trae.title(), 'telefono_que_lo_trae':alumno.telefono_que_lo_trae})
    return render(request, 'modificar_alumno.html', {'alumno_form':alumno_form, 'dni_alumno':dni_alumno})

@user_passes_test(check_Secretaria)
def form_editar_padre(request, dni_padre):
    objetivo = "Editar"
    padre = Padre_madre.objects.get(dni=dni_padre)
    padre_form =EditarPadreForm(initial={'nombre':padre.nombre.title(), 'apellido':padre.apellido.title(),'lugar_nacimiento':padre.lugar_nacimiento,'fecha_nacimiento':padre.fecha_nacimiento,'domicilio':padre.domicilio.title(),'email':padre.email, 'sexo':padre.sexo, 'profesion':padre.profesion.title(), 'telefono_trabajo':padre.telefono_trabajo})
    return render(request, 'Padre_madre/crear_padre_madre.html', {'padre_form':padre_form, 'objetivo':objetivo, 'dni_padre':padre.dni})

@user_passes_test(check_Secretaria)
def form_editar_transportista(request, dni_transportista):
    transportista = Transportista.objects.get(dni=dni_transportista)
    opcion = "Editar"
    form_transportista = EditarTransportistaForm(initial={'nombre':transportista.nombre.title(),'apellido':transportista.apellido.title(), 'lugar_nacimiento':transportista.lugar_nacimiento.title(),'fecha_nacimiento':transportista.fecha_nacimiento,'domicilio':transportista.domicilio.title(),'email':transportista.email,'sexo':transportista.sexo,'nombre_transporte':transportista.nombre_transporte.title(),'telefono_transportista':transportista.telefono_transportista,'detalles_transportista':transportista.detalles_transportista})
    return render(request, 'Transportista/crear_transportista.html', {'form_transportista':form_transportista, 'opcion':opcion, 'dni_transportista':transportista.dni})

@user_passes_test(check_Secretaria)
def form_editar_autorizado(request, dni_autorizado):
    autorizado_elegido = Autorizado.objects.get(dni=dni_autorizado)
    opcion = "Editar"
    autorizado = EditarAutorizadoForm(initial={'nombre':autorizado_elegido.nombre.title(),'apellido':autorizado_elegido.apellido.title(),'lugar_nacimiento':autorizado_elegido.lugar_nacimiento.title(),'fecha_nacimiento':autorizado_elegido.fecha_nacimiento,'domicilio':autorizado_elegido.domicilio.title(),'email':autorizado_elegido.email,'sexo':autorizado_elegido.sexo,'telefono_autorizado':autorizado_elegido.telefono_autorizado})
    return render(request, 'Autorizado/crear_autorizado.html', {'autorizado':autorizado, 'opcion':opcion, 'dni':autorizado_elegido.dni})
    
@user_passes_test(check_Admin_s)
def form_editar_datos(request):
    editar_f = datos_Index.objects.get(pk=1)
    form = EditarIndexForm(initial={'telefono':editar_f.telefono,'telefono2':editar_f.telefono2,'email':editar_f.email,'email2':editar_f.email2,'latitud':editar_f.latitud,'longitud':editar_f.longitud})
    return render(request, 'Admin_Secretaria/form_datos_index.html', {'form':form})
    
"""
=========
Creacion.
=========
"""

#Funcion que Crea al Alumno.
def crear_alumno(request):
    alumno_form = AlumnoForm(request.POST)
    if alumno_form.is_valid():
        alumno_form.save()
        dni_alumno = alumno_form.cleaned_data['dni']
        apellido_alumno = alumno_form.cleaned_data['apellido']
        nombre_alumno = alumno_form.cleaned_data['nombre']
        alumno = Alumno.objects.get(dni=dni_alumno)
        datos_alumno = {
            'dni_alumno':dni_alumno,
            'apellido_alumno':apellido_alumno,
            'nombre_alumno':nombre_alumno
        }
        new_nombre = nombre_alumno.lower()
        new_apellido = apellido_alumno.lower()
        alumno.nombre, alumno.apellido = new_nombre, new_apellido
        alumno.save()
        matriculacion = Matriculacion(alumno=alumno, matriculado="No")
        matriculacion.save()
        padre_form = PadreForm()
        return render(request, 'Padre_madre/cargar_padre.html', {'padre_form':padre_form, 'datos_alumno':datos_alumno})
    else:
        aux = alumno_form.errors
        return HttpResponse(str(aux))
    
def crear_trabajador(request):
    trabajador = ProfesorForm(request.POST)
    if trabajador.is_valid():
        new_nombre = trabajador.cleaned_data['nombre_t']
        new_apellido = trabajador.cleaned_data['apellido_t']
        dni = trabajador.cleaned_data['dni_t']
        lugar_nacimiento = trabajador.cleaned_data['lugar_nacimiento_t']
        fecha_nacimiento = trabajador.cleaned_data['fecha_nacimiento_t']
        domicilio = trabajador.cleaned_data['domicilio_t']
        email = trabajador.cleaned_data['email_t']
        sexo = trabajador.cleaned_data['sexo_t']
        telefono_particular = trabajador.cleaned_data['telefono_particular']
        telefono_laboral = trabajador.cleaned_data['telefono_laboral']
        telefono_familiar = trabajador.cleaned_data['telefono_familiar']
        datos_familiares_cargo = trabajador.cleaned_data['datos_familiares_cargo']
        antecedentes_laborales = trabajador.cleaned_data['antecedentes_laborales']
        estudios_cursados = trabajador.cleaned_data['estudios_cursados']
        cargo = request.POST['cargo']
        nombre = new_nombre.lower()
        apellido = new_apellido.lower()
        grupo = 0
        try:
            trabajador = Trabajador.objects.get(dni_t=dni)
            data = {
                'error':True,
                'resultado': 'Ya existe un Trabajador con ese Dni.'
            }
            return JsonResponse(data)
        except Trabajador.DoesNotExist:
            try:
                trabajador = Trabajador.objects.get(email_t=email)
                data = {
                    'error':True,
                    'resultado': 'Ya existe un Trabajador con esa direccion de Email.'
                }
                return JsonResponse(data)
            except Trabajador.DoesNotExist:
                trabajadorr = Trabajador(nombre_t= nombre, apellido_t=apellido,dni_t=dni,lugar_nacimiento_t=lugar_nacimiento, fecha_nacimiento_t=fecha_nacimiento,domicilio_t=domicilio,email_t=email,sexo_t=sexo, telefono_particular=telefono_particular, telefono_laboral=telefono_laboral, telefono_familiar=telefono_familiar, datos_familiares_cargo=datos_familiares_cargo, antecedentes_laborales=antecedentes_laborales, estudios_cursados=estudios_cursados, cargo_t=cargo)
                trabajadorr.save()
                username = trabajadorr.create_username()
                password = trabajadorr.create_pass_user()
                user = User.objects.create_user(username=username, password=password)
                if (grupo == 0):
                    grupo = Group.objects.get(name='Secretaria')
                    grupo.user_set.add(user)
                else:
                    user = User.objects.create_user(username=username, password=password)
                    grupo = Group.objects.get(name='Director')

                user_S = user_Trabajador(user=user, trabajador=trabajadorr)
                user_S.save()
                subject = "Usuario Creado"
                message = "Sus datos han sido ingresados al sistema, en el cual utilizara  " + str(username) + " como nombre de usuario, y  " + str(password) + " como password para acceder."
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [trabajadorr.email_t]
                send_mail(subject, message, email_from, recipient_list)
                data = {
                    'error':False,
                    'resultado': " Datos cargados con exito."
                }
                return JsonResponse(data)
    else:
        aux = trabajador.errors
        data = {
            'error':True,
            'resultado':str(aux)
        }
        return JsonResponse(data)

def definir_curso(seccion):
    if (seccion == "B" or seccion == "D"):
        print ("Es B o D")
        return True
    else: 
        print ("Es A o C")
        return False
        
    # HORA: TRUE, SECCION TRUE: --- D
    # HORA: FALSE, SECCION TRUE: ---- B
    # HORA: TRUE, SECCION FALSE: ---- C
    # HORA: FALSE, SECCION FALSE: ----- A
    
def crear_curso(request):
    if request.method == "POST":
        aNo = request.POST['año']
        seccion = request.POST['division']
        hora = request.POST['hora']
        if hora == "AB":
            print ("Es A o B")
            hora = False
        else:
            hora = True
            print ("Es C o D")
        seccion = definir_curso(seccion)
        print (hora)
        print (seccion)
        curso, created = Curso.objects.get_or_create(aNo=aNo, seccion=seccion, hora=hora)
        if (created == False):
            msg = "Ya existe este cuso"
        else:
            msg = "El curso " + str(curso) + " ha sido creado con exito."
        data = {
            'resultado': msg
        }
        return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

def crear_autorizado(request):
    autorizado_form = AutorizadoForm(request.POST)
    if autorizado_form.is_valid():
        autorizado_form.save()
        dni_autorizado = autorizado_form.cleaned_data['dni']
        nombre = autorizado_form.cleaned_data['nombre']
        apellido = autorizado_form.cleaned_data['apellido']
        autorizado = Autorizado.objects.get(dni=dni_autorizado)
        subject = "Inicio de Sesion."
        message = "En el dia de la fecha se le notifica que sus datos han sido cargados en nuestra pagina."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [autorizado.email]
        send_mail( subject, message, email_from, recipient_list)
        data = {
            'error':False,
            'resultado': " Los datos de " + nombre.title() + " " + apellido.title() + " han sido cargados con exito."
        }
        new_nombre = nombre.lower()
        new_apellido = apellido.lower()
        autorizado.nombre, autorizado.apellido = new_nombre, new_apellido
        autorizado.save()
        return JsonResponse(data)
    else:
        resultado = str(autorizado_form.errors)
        data = {
            'error':True,
            'resultado':resultado
        }
        return JsonResponse(data)
        
#Funcoin que crea al Padre.
def crear_padre(request):
    padre_form = PadreForm(request.POST)
    dni_alumno = request.POST['dni_alumno']
    alumno = Alumno.objects.get(dni=dni_alumno)
    if padre_form.is_valid():
        padre_form.save()
        dni_padre = padre_form.cleaned_data['dni']
        padre = Padre_madre.objects.get(dni=dni_padre)
        resultado = "El pedido de Matriculacion de " + str(alumno.apellido.title()) + " " + str(alumno.nombre.title()) + " ha sido creado con exito, y los datos de " + str(padre.apellido.title()) + " " + str(padre.nombre.title()) + " han sido ingresados al sistema."
        data = {
            'error': False,
            'resultado':resultado
        }
        nombre = padre_form.cleaned_data['nombre']
        apellido = padre_form.cleaned_data['apellido']
        new_nombre = nombre.lower()
        new_apellido = apellido.lower()
        padre.nombre, padre.apellido = new_nombre, new_apellido
        padre.save()
        familia = Familia(alumno=alumno, padre_madre=padre)
        familia.save()
        new_Matriculacion = Matriculacion.objects.get(alumno=alumno)
        new_Matriculacion.matriculado="No"
        new_Matriculacion.save()
        return JsonResponse(data)
    else:
        resultado = str(padre_form.errors)
        data = {
            'error':True,
            'resultado':resultado
        }
        return JsonResponse(data)
    
def crear_padre_madre(request):
    if request.method == "POST":
        padre_form = PadreForm(request.POST)
        if padre_form.is_valid():
            print ("Es valido")
            padre_form.save()
            dni_padre = padre_form.cleaned_data['dni']
            padre = Padre_madre.objects.get(dni=dni_padre)
            nombre = padre_form.cleaned_data['nombre']
            apellido = padre_form.cleaned_data['apellido']
            new_nombre = nombre.lower()
            new_apellido = apellido.lower()
            resultado = "El Padre " + str(padre.apellido.title()) + " " + str(padre.nombre.title()) + " ha sido creado con exito."
            data = {
                'error':False,
                'resultado':resultado
            }
            padre.nombre, padre.apellido = new_nombre, new_apellido
            padre.save()
            return JsonResponse(data)
        else:
            print ("No es valido")
            resultado = str(padre_form.errors)
            print (resultado)
            data = {
                'error':True,
                'resultado':resultado
            }
            return JsonResponse(data)
    else:
        return HttpResponse("Solo podes acceder por Post")

#Funcion que Crea al Transportista.
def crear_transportista(request):
    if request.method == 'POST':
        form_transportista = TransportistaForm(request.POST)
        if form_transportista.is_valid():
            form_transportista.save()
            nombre = form_transportista.cleaned_data['nombre']
            apellido = form_transportista.cleaned_data['apellido']
            dni = form_transportista.cleaned_data['dni']
            transportista = Transportista.objects.get(dni=dni)
            new_nombre = nombre.lower()
            new_apellido = apellido.lower()
            data = {
                'error':False,
                'resultado': 'El transportista ' + str(transportista.nombre.title()) + ' ' + str(transportista.apellido.title()) + ' ha sido cargado con exito.'
            }
            transportista.nombre, transportista.apellido = new_nombre, new_apellido
            transportista.save()
            return JsonResponse(data)
        else:
            data = {
                'error':True,
                'resultado':str(form_transportista.errors)
            }
            return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

def crear_obra_social(request):
    if request.method=="POST":
        form_obra_s = Obra_SocialForm(request.POST)
        if form_obra_s.is_valid():
            form_obra_s.save()
            data = {
                'error':False,
                'resultado': 'Obra Social creada con exito.'
            }
            return JsonResponse(data)
        else:
            data = {
                'error':True,
                'resultado':str(form_obra_s.errors)
            }
            return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

#Funcion que crea una instancia de la Tabla Intermedia entre Alumno y Transportista.
def asignar_transportista(request):
    if request.method == 'POST':
        dni = request.POST['dni_alumno']
        dni_transportista = request.POST['dni_transportista']
        alumno = Alumno.objects.get(dni=dni)
        transportista = Transportista.objects.get(dni=dni_transportista)
        try:
            usa_transporte = usa_Transporte.objects.get(alumno=alumno, transportista=transportista)
            usa_transporte.habilitado = True
            usa_transporte.save()
        except usa_Transporte.DoesNotExist:
            usa_transporte = usa_Transporte(alumno=alumno, transportista=transportista)
            usa_transporte.save()
        data = {
            'resultado': 'Transportista asignado con exito.'
        }
        return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

#Funcion que crea una instancia de la Tabla Intermedia entre Alumno y Padre/Madre.
def asignar_padre(request):
    if request.method == 'POST':
        dni = request.POST['dni_alumno']
        dni_padre = request.POST['dni_padre']
        alumno = Alumno.objects.get(dni=dni)
        padre = Padre_madre.objects.get(dni=dni_padre)
        try:
            familia = Familia.objects.get(alumno=alumno, padre_madre=padre)
            familia.habilitado = True
            familia.save()
        except Familia.DoesNotExist:
            familia = Familia(alumno=alumno, padre_madre=padre)
            familia.save()
        data = {
            'resultado': 'Padre asignado con exito.'
        }
        return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

def asignar_obra_social(request):
    if request.method == 'POST':
        dni = request.POST['dni_alumno']
        id_obra_social = request.POST['id_obra_social']
        num_afiliado = request.POST['num_afiliado']
        alumno = Alumno.objects.get(dni=dni)
        obra_Social = Obra_Social.objects.get(id=id_obra_social)
        try:
            usa_Obra = usa_Obra_Social.objects.get(alumno=alumno, obra_social=obra_Social)
            usa_Obra.numero_afiliado = num_afiliado
            usa_Obra.habilitado = True
            usa_Obra.save()
        except usa_Obra_Social.DoesNotExist:
            usa_Obra = usa_Obra_Social(alumno=alumno, obra_social=obra_Social, numero_afiliado=num_afiliado)
            usa_Obra.save()
        data = {
            'resultado':"Obra Asignada con exito."
        }
        return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

def asignar_autorizado(request):
    if request.method == 'POST':
        dni = request.POST['dni_alumno']
        dni_autorizado = request.POST['dni_autorizado']
        relacion_con_alumno = RelacionForm(request.POST)
        if relacion_con_alumno.is_valid():
            relacion_con_alumno = relacion_con_alumno.cleaned_data['relacion_con_alumno']
            alumno = Alumno.objects.get(dni=dni)
            autorizado = Autorizado.objects.get(dni=dni_autorizado)
            try:
                alumno_autorizado = alumno_Autorizado.objects.get(alumno=alumno, autorizado=autorizado)
                alumno_autorizado.relacion_con_alumno = relacion_con_alumno
                alumno_autorizado.habilitado = True
                alumno_autorizado.save()
            except alumno_Autorizado.DoesNotExist:
                alumno_autorizado = alumno_Autorizado(alumno=alumno, autorizado=autorizado, relacion_con_alumno=relacion_con_alumno)
                alumno_autorizado.save()
            data = {
                'resultado':"Autorizado Asignado con exito."
            }
            return JsonResponse(data)
        else:
            data = {
                'resultado':str(relacion_con_alumno.errors)
            }
            return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

"""
========================================
Traer Todas las instancias de un modelo.
========================================
"""

#Traer Todos los Transnportistas.
def todos_los_transportistas_asignar(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    transportistas_ya_asignados = usa_Transporte.objects.filter(alumno=alumno, habilitado=True)
    lista = []
    for a in transportistas_ya_asignados:
        lista.append(a.transportista.dni)
    transportistas = Transportista.objects.exclude(dni__in=lista).order_by("nombre","apellido","dni")
    return render(request, 'Transportista/asignar_transportista.html',{'transportistas':transportistas, 'dni_alumno':dni_alumno})

#Traer Todos los Padres/Madre.
def todos_los_padres_asignar(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    padres_ya_asignados = Familia.objects.filter(alumno=alumno, habilitado=True)
    lista = []
    for a in padres_ya_asignados:
        lista.append(a.padre_madre.dni)
    padre = Padre_madre.objects.exclude(dni__in=lista).order_by("nombre","apellido","dni")
    return render(request,'Padre_madre/asignar_padre.html', {'todos_los_padres':padre, 'dni_alumno':dni_alumno})

def asignar_obra(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    obras_ya_asignadas = usa_Obra_Social.objects.filter(alumno=alumno, habilitado=True)
    lista = []
    for a in obras_ya_asignadas:
        lista.append(a.obra_social.id)
    obra_social = Obra_Social.objects.exclude(id__in=lista).order_by("nombre")
    obra_social2 = Obra_SocialForm()
    return render(request,'Obra_Social/asignar_obra.html', {'obras_sociales':obra_social, 'dni_alumno':dni_alumno, 'obra_social':obra_social2})


def todos_los_autorizados_asignar(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    autorizados_ya_asignadas = alumno_Autorizado.objects.filter(alumno=alumno, habilitado=True)
    print(autorizados_ya_asignadas)
    lista = []
    for a in autorizados_ya_asignadas:
        lista.append(a.autorizado.dni)
    autorizados = Autorizado.objects.exclude(dni__in=lista).order_by("nombre","apellido","dni")
    relacion_con_alumno = RelacionForm()
    print(autorizados)
    return render(request,'Autorizado/asignar_autorizado.html', {'autorizados':autorizados, 'alumno':alumno, 'relacion_con_alumno':relacion_con_alumno})

@user_passes_test(check_Secretaria)
def todas_las_obras_sociales(request):
    obra_social = Obra_Social.objects.all()
    return render(request, 'Obra_Social/todas_las_obras_sociales.html', {'obras_sociales':obra_social})

@user_passes_test(check_Secretaria)
def todas_los_transportistas(request):
    transportistas = Transportista.objects.all().order_by("nombre","apellido","dni")
    return render(request, 'Transportista/todos_los_transportistas.html', {'transportistas':transportistas})

#Traer Todos las Matriculaciones con estado 'No' y 'Re'.
@user_passes_test(check_Secretaria)
def traer_pedidos(request):
    matriculaciones = Matriculacion.objects.filter(matriculado="No").order_by('-fecha_matriculacion')
    re_matriculaciones = Matriculacion.objects.filter(matriculado = "Re").order_by('-fecha_matriculacion')
    egresos = Matriculacion.objects.filter(matriculado="Pe").order_by('-fecha_matriculacion')
    return render(request, 'pedidos.html', {'matriculaciones':matriculaciones, 're_matricular':re_matriculaciones, 'egresos':egresos})

def padres_del_alumno(request, opcion, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    if (opcion == "pedido"):
        alumno.opcion = "pedido"
    else:
        alumno.opcion = "perfil"
    familia = Familia.objects.filter(alumno=alumno, habilitado=True).order_by("padre_madre__apellido", "padre_madre__nombre", "padre_madre__dni")
    return render(request, 'Padre_madre/padres_del_alumno.html', {'familiares':familia, 'alumno':alumno})

def transportistas_del_alumno(request, opcion, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    if (opcion == "pedido"):
        alumno.opcion = "pedido"
    else:
        alumno.opcion = "perfil"
    transportistas = usa_Transporte.objects.filter(alumno=alumno, habilitado=True).order_by("transportista__apellido", "transportista__nombre", "transportista__dni")
    return render(request, 'Transportista/transportistas_del_alumno.html', {'transportistas':transportistas, 'alumno':alumno})

def obras_sociales_del_alumno(request,opcion, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    if (opcion == "pedido"):
        alumno.opcion = "pedido"
    else:
        alumno.opcion = "perfil"
    obras_sociales = usa_Obra_Social.objects.filter(alumno=alumno, habilitado=True)
    return render(request, 'Obra_Social/obras_sociales_del_alumno.html', {'obras_sociales':obras_sociales, 'alumno':alumno})

def autorizados_del_alumno(request, opcion, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    if (opcion == "pedido"):
        alumno.opcion = "pedido"
    else:
        alumno.opcion = "perfil"
    autorizados = alumno_Autorizado.objects.filter(alumno=alumno, habilitado=True).order_by("autorizado__apellido", "autorizado__nombre", "autorizado__dni")
    return render(request, 'Autorizado/autorizados_del_alumno.html', {'autorizados':autorizados, 'alumno':alumno})

@user_passes_test(check_Admin_s)
def trabajador_sd(request, cargo):
    if (cargo == 'Secretarias'):
        msg = "Secretaria"
        trabajadores = Trabajador.objects.filter(cargo_t="SE")
    else:
        msg = "Director"
        trabajadores = Trabajador.objects.filter(cargo_t="DI")
    return render(request, 'Admin_Secretaria/tabla.html', {'cargo':cargo,'trabajadores':trabajadores, 'msg':msg})
    

"""
===================================
Mostrar los datos de una instancia.
===================================
"""

#Funcion que Trae los datos del Transportista elegido previamente
def datos_transportista(request, dni_transportista):
    transportista = Transportista.objects.get(dni=dni_transportista)
    return render(request, 'Transportista/datos_transportista.html', {'transportista':transportista})

def datos_autorizado(request, dni_transportista):
    autorizado = Autorizado.objects.get(dni=dni_transportista)
    return render(request, 'Autorizado/datos_autorizado.html', {'autorizado':autorizado})

def usuarios_transportista(request, dni_transportista):
    transportista = Transportista.objects.get(dni=dni_transportista)
    todos_los_alumnos = usa_Transporte.objects.filter(transportista=transportista).order_by(alumno)
    return render(request, 'Transportista/usuarios_transportista.html', {'transportista':transportista, 'todos_los_alumnos':todos_los_alumnos})

def datus_usuario_t(request, dni_trabajador):
    trabajador = Trabajador.objects.get(dni_t=dni_trabajador)
    user_T = user_Trabajador.objects.get(trabajador=trabajador)
    return render(request, 'Admin_Secretaria/user_trabajador.html', {'trabajador':user_T})
    
#Funcion que Trae los datos del Padre elegido previamente
def datos_padre(request, dni_padre):
    padre = Padre_madre.objects.get(dni=dni_padre)
    return render(request, 'Padre_madre/datos_padre.html', {'padre':padre})

def datos_obra_social(request, id_obra_social):
    obra_social = Obra_Social.objects.get(pk=id_obra_social)
    todos_los_alumnos = usa_Obra_Social.objects.filter(obra_social=obra_social).order_by("alumno__nombre","alumno__nombre","alumno__dni")
    return render(request, 'Obra_Social/datos_obra_social.html', {'todos_los_alumnos':todos_los_alumnos, 'obra_social':obra_social})

#Funcion que Trae los datos del Alumno elegido previamente
@login_required
def perfil_alumno(request, opcion, dni_alumno):
    print (opcion)
    alumno = Alumno.objects.get(dni=dni_alumno)
    matriculacion = Matriculacion.objects.get(alumno=alumno)
    estado = matriculacion.get_Estado()
    alumno.estado = estado

    alumno.curso_si = matriculacion.curso
    if (opcion == 'pedidos'):
        alumno.opcion = "pedido"
    else:
        alumno.opcion = "curso"
    return render(request, 'perfilAlumno.html', {'alumno':alumno})

#Funcion que Trae los Familiares, Transportistas del Alumno y los Cursos.
def get_Secciones(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    familiares = Familia.objects.filter(alumno=alumno, habilitado=True).order_by("padre_madre__apellido", "padre_madre__nombre")
    transportistas = usa_Transporte.objects.filter(alumno=alumno, habilitado=True)
    cursos = Curso.objects.all().order_by("aNo", "hora","seccion")
    obras_sociales = usa_Obra_Social.objects.filter(alumno=alumno, habilitado=True)
    autorizados = alumno_Autorizado.objects.filter(alumno=alumno, habilitado=True)
    return render(request, 'matricular.html', {'familiares':familiares, 'alumno':alumno, 'cursos':cursos, 'transportistas':transportistas, 'obras_sociales':obras_sociales, 'autorizados':autorizados})

#Funcion que Trae los Familiares, Transportistas, Curso Actual del Alumno y los Cursos.
def re_matricular(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    familiares = Familia.objects.filter(alumno=alumno, habilitado=True).order_by("padre_madre__apellido", "padre_madre__nombre")
    transportistas = usa_Transporte.objects.filter(alumno=alumno, habilitado=True)
    curso2 = Matriculacion.objects.get(alumno=alumno)
    curso = curso2.curso
    obras_sociales = usa_Obra_Social.objects.filter(alumno=alumno, habilitado=True)
    autorizados = alumno_Autorizado.objects.filter(alumno=alumno, habilitado=True)
    recomendacion, created = Curso.objects.get_or_create(aNo=curso.aNo+1, hora=curso.hora, seccion=curso.seccion)
    lista = []
    lista.append(curso.id)
    lista.append(recomendacion.id)
    cursos = Curso.objects.exclude(id__in=lista).order_by("aNo", "-hora")
    return render(request, 'Re_matricular/re_matricular.html', {'familiares':familiares, 'alumno':alumno, 'cursos':cursos, 'transportistas':transportistas, 'curso':curso, 'recomendacion':recomendacion, 'obras_sociales':obras_sociales, 'autorizados':autorizados})

def egresar(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    return render(request, 'egresar.html', {'alumno':alumno})

"""
==========
Modificar.
==========
"""

def pedido_egreso(request):
    if request.method == "POST":
        dni_alumno = request.POST['dni_alumno']
        alumno = Alumno.objects.get(dni=dni_alumno)
        matriculacion = Matriculacion.objects.get(alumno=alumno)
        matriculacion.matriculado = "Pe"
        matriculacion.save()
        familiares = Familia.objects.filter(alumno=alumno, habilitado=True)
        subject = "Pedido de Egresso de " + str(alumno.apellido) + " " + str(alumno.nombre) + "."
        secretaria = user_Trabajador.objects.get(user=request.user)
        message = "Se le notifica que la Secretaria " + secretaria.trabajador.apellido_t + " " + secretaria.trabajador.nombre_t + " ha creado un pedido de Egreso para su hijo/a " + alumno.apellido + " " +  alumno.nombre + "."
        email_from = settings.EMAIL_HOST_USER
        for familiar in familiares:
            recipient_list = [familiar.padre_madre.email]
            send_mail( subject, message, email_from, recipient_list)
        data = {
            'resultado': " El pedido de egreso de " + alumno.nombre.title() + " ha sido un exito."
        }
        return JsonResponse(data)
    return HttpResponse("Solo podes entrar por POST")

@user_passes_test(check_Admin_s)
def cambiar_datos(request):
    if request.method == 'POST':
        datos_form = EditarIndexForm(request.POST)
        if datos_form.is_valid():
            telefono = datos_form.cleaned_data['telefono']
            telefono2 = datos_form.cleaned_data['telefono2']
            email = datos_form.cleaned_data['email']
            email2 = datos_form.cleaned_data['email2']
            latitud = datos_form.cleaned_data['latitud']
            longitud = datos_form.cleaned_data['longitud']
            editar_f = datos_Index.objects.get(pk=1)
            editar_f.telefono, editar_f.telefono2, editar_f.email, editar_f.email2, editar_f.latitud, editar_f.longitud = telefono, telefono2, email, email2, latitud, longitud
            editar_f.save()
            return redirect ('form_editar_datos')
        return redirect ('form_editar_datos')
    else:
        return HttpResponse("Solo podes entrar por POST")

def editar_padre(request):
    if request.method == 'POST':
        padre_form = EditarPadreForm(request.POST)
        if padre_form.is_valid():
            dni_p = request.POST['dni_padre']
            padre = Padre_madre.objects.get(dni=dni_p)
            nombre = padre_form.cleaned_data['nombre']
            apellido = padre_form.cleaned_data['apellido']
            nuevo_lugar_nacimiento = padre_form.cleaned_data['lugar_nacimiento']
            nueva_fecha_nacimiento = padre_form.cleaned_data['fecha_nacimiento']
            nuevo_domicilio = padre_form.cleaned_data['domicilio']
            nuevo_email = padre_form.cleaned_data['email']
            nuevo_sexo = padre_form.cleaned_data['sexo']
            nuevo_profesion = padre_form.cleaned_data['profesion']
            telefono_trabajo = padre_form.cleaned_data['telefono_trabajo']
            nuevo_nombre = nombre.lower()
            nuevo_apellido = apellido.lower()
            padre.nombre, padre.apellido, padre.lugar_nacimiento, padre.fecha_nacimiento, padre.domicilio, padre.email, padre.sexo, padre.profesion, padre.telefono_trabajado = nuevo_nombre, nuevo_apellido, nuevo_lugar_nacimiento, nueva_fecha_nacimiento, nuevo_domicilio, nuevo_email, nuevo_sexo, nuevo_profesion, telefono_trabajo
            subject = "Perfil Modificado."
            secretaria = user_Trabajador.objects.get(user=request.user)
            message = "Se le notifica que la Secretaria " + secretaria.trabajador.apellido_t.title() + " " + secretaria.trabajador.nombre_t.title() + " ha realizado cambios en su perfil."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [padre.email]
            send_mail( subject, message, email_from, recipient_list)
            padre.save()
            data = {
                'error':False,
                'resultado': " Los Datos de " + padre.nombre.title() + " " + padre.apellido.title() + " han sido modificados con exito."
            }
            return JsonResponse(data)
        else:
            data = {
                'error':True,
                'resultado':str(padre_form.errors)
            }
            return JsonResponse(data)
    else:
        return HttpResponse("Solo podes entrar por POST")

@user_passes_test(check_Secretaria)
def editar_autorizado(request):
    if request.method == 'POST':
        autorizado = EditarAutorizadoForm(request.POST)
        if autorizado.is_valid():
            dni_t = request.POST['dni']
            autorizado_elegido = Autorizado.objects.get(dni=dni_t)
            nombre = autorizado.cleaned_data['nombre']
            apellido = autorizado.cleaned_data['apellido']
            nuevo_lugar_nacimiento = autorizado.cleaned_data['lugar_nacimiento']
            nueva_fecha_nacimiento = autorizado.cleaned_data['fecha_nacimiento']
            nuevo_domicilio = autorizado.cleaned_data['domicilio']
            nuevo_email = autorizado.cleaned_data['email']
            nuevo_sexo = autorizado.cleaned_data['sexo']
            nuevo_telefono_autorizado = autorizado.cleaned_data['telefono_autorizado']
            
            nuevo_nombre = nombre.lower()
            nuevo_apellido = apellido.lower()
        
            autorizado_elegido.nombre = nuevo_nombre
            autorizado_elegido.apellido = nuevo_apellido
            autorizado_elegido.lugar_nacimiento = nuevo_lugar_nacimiento
            autorizado_elegido.fecha_nacimiento = nueva_fecha_nacimiento
            autorizado_elegido.domicilio = nuevo_domicilio
            autorizado_elegido.email = nuevo_email
            autorizado_elegido.sexo = nuevo_sexo
            autorizado_elegido.telefono_autorizado = nuevo_telefono_autorizado 
        
            autorizado_elegido.save()
            data = {
                'error': False,
                'resultado': " Los Datos de " + autorizado_elegido.nombre.title() + " " + autorizado_elegido.apellido.title() + " han sido modificados con exito."
            }
            return JsonResponse(data)
        else:
            data = {
                'error':True,
                'resultado':str(autorizado.errors)
            }
            return JsonResponse(data)
    else:
        return HttpResponse("Solo podes entrar por POST")
    
@user_passes_test(check_Secretaria)
def editar_transportista(request):
    if request.method == 'POST':
        form_transportista = EditarTransportistaForm(request.POST)
        if form_transportista.is_valid():
            dni_t = request.POST['dni_transportista']
            transportista = Transportista.objects.get(dni=dni_t)
            nombre = form_transportista.cleaned_data['nombre']
            apellido = form_transportista.cleaned_data['apellido']
            nuevo_lugar_nacimiento = form_transportista.cleaned_data['lugar_nacimiento']
            nueva_fecha_nacimiento = form_transportista.cleaned_data['fecha_nacimiento']
            nuevo_domicilio = form_transportista.cleaned_data['domicilio']
            nuevo_email = form_transportista.cleaned_data['email']
            nuevo_sexo = form_transportista.cleaned_data['sexo']
            nuevo_nombre_transporte = form_transportista.cleaned_data['nombre_transporte']
            nuevo_telefono_transportista = form_transportista.cleaned_data['telefono_transportista']
            nuevo_detalles_transportista = form_transportista.cleaned_data['detalles_transportista']
            nuevo_nombre = nombre.lower()
            nuevo_apellido = apellido.lower()
            transportista.nombre, transportista.apellido, transportista.lugar_nacimiento, transportista.fecha_nacimiento, transportista.domicilio, transportista.email, transportista.sexo,transportista.nombre_transporte, transportista.telefono_transportista, transportista.detalles_transportista = nuevo_nombre, nuevo_apellido, nuevo_lugar_nacimiento, nueva_fecha_nacimiento, nuevo_domicilio, nuevo_email, nuevo_sexo,nuevo_nombre_transporte,nuevo_telefono_transportista,nuevo_detalles_transportista
            transportista.save()
            data = {
                'error':False,
                'resultado': " Los Datos de " + transportista.nombre.title() + " " + transportista.apellido.title() + " han sido modificados con exito."
            }
            return JsonResponse(data)
        else:
            data = {
                'error':True,
                'resultado':str(form_transportista.errors)
            }
            return JsonResponse(data)
    else:
        return HttpResponse("Solo podes entrar por POST")

def aceptar_re_matriculacion(request):
    if request.method == "POST":
        dni_alumno = request.POST['dni_alumno2']
        selected_curso = request.POST['select_curso2']
        curso = Curso.objects.get(id=selected_curso)
        alumno = Alumno.objects.get(dni=dni_alumno)
        matriculacion = Matriculacion.objects.get(alumno=alumno)
        matriculacion.curso = curso
        matriculacion.matriculado = "Si"
        matriculacion.save()
        familiares = Familia.objects.filter(alumno=alumno, habilitado=True)
        subject = "Pedido de Re Matriculacion de " + str(alumno.apellido.title()) + " " + str(alumno.nombre.title()) + "."
        secretaria = user_Trabajador.objects.get(user=request.user)
        message = "Se le notifica que la Secretaria " + secretaria.trabajador.apellido_t.title() + " " + secretaria.trabajador.nombre_t.title() + " ha aceptado el pedido de Re Matriculacion de su hijo/a " + alumno.apellido.title() + " " + alumno.nombre.title() + ", el cual ahora asistira a " + str(matriculacion.curso) + "."
        email_from = settings.EMAIL_HOST_USER
        for familiar in familiares:
            recipient_list = [familiar.padre_madre.email]
            send_mail( subject, message, email_from, recipient_list)
        data = {
            'error':False,
            'resultado': " El pedido de Re Matriculacion de " + alumno.nombre.title() + " ha sido un exito, ahora " + alumno.nombre.title() + " asiste a " + str(matriculacion.curso) + "."
        }
        return JsonResponse(data)
    return HttpResponse("Solo podes entrar por POST")

def egresar_alumno(request):
    if request.method == "POST":
        dni_alumno = request.POST['dni_alumno']
        alumno = Alumno.objects.get(dni=dni_alumno)
        matriculacion = Matriculacion.objects.get(alumno=alumno)
        matriculacion.matriculado = "Eg"
        matriculacion.fecha_matriculacion = datetime.date.today()
        matriculacion.save()
        familiares = Familia.objects.filter(alumno=alumno, habilitado=True)
        subject = "Pedido de Egreso de " + str(alumno.apellido.title()) + " " + str(alumno.nombre.title()) + "."
        secretaria = user_Trabajador.objects.get(user=request.user)
        message = "Se le notifica que la Secretaria " + secretaria.trabajador.apellido_t.title() + " " + secretaria.trabajador.nombre_t.title() + " ha aceptado el pedido de Egreso de su hijo/a " + alumno.apellido.title() + " " + alumno.nombre.title() + "."
        email_from = settings.EMAIL_HOST_USER
        for familiar in familiares:
            recipient_list = [familiar.padre_madre.email]
            send_mail( subject, message, email_from, recipient_list)
        data = {
            'error':False,
            'resultado': " El pedido de Egreso de " + alumno.nombre.title() + " ha sido un exito."
        }
        return JsonResponse(data)


def pedido_re_matricular(request):
    if request.method == "POST":
        re_matricular_form = ReMatricularForm(request.POST)
        if re_matricular_form.is_valid():
            dni_alumno = re_matricular_form.cleaned_data['dni_alumno']
            dni_padre = re_matricular_form.cleaned_data['dni_padre']
            email_padre = re_matricular_form.cleaned_data['email_padre']
            try:
                alumno = Alumno.objects.get(dni=dni_alumno)
                matriculacion = Matriculacion.objects.get(alumno=alumno)
                if matriculacion.matriculado == "No":
                    data = {
                        'error':True,
                        'resultado': " Este Alumno no se encuentra disponible para Re Matricular."
                    }
                    return JsonResponse(data)
                elif matriculacion.matriculado == "Re":
                    data = {
                        'error':True,
                        'resultado': " Ya hay un pedido de Re Matriculacion para este Alumno."
                    }
                    return JsonResponse(data)
                else:
                    try:
                        padre = Padre_madre.objects.get(dni=dni_padre)
                        if (padre.email == email_padre):
                            familiares = Familia.objects.filter(alumno=alumno, habilitado=True)
                            subject = "Pedido de Re Matriculacion de " + str(alumno.apellido.title()) + " " + str(alumno.nombre.title()) + "."
                            message = "En el dia de la fecha " + str(padre.apellido.title()) + " " + str(padre.nombre.title()) + " ha solicitado un pedido de re matriculacion para " + str(alumno.apellido.title()) + " " + str(alumno.nombre.title()) + "."
                            email_from = settings.EMAIL_HOST_USER
                            for familiar in familiares:
                                print ("Enviando EMail")
                                recipient_list = [familiar.padre_madre.email]
                                send_mail( subject, message, email_from, recipient_list)

                            matriculacion = Matriculacion.objects.get(alumno=alumno)
                            matriculacion.matriculado = "Re"
                            matriculacion.save()
                            data = {
                                'error':False,
                                'resultado': " El pedido de Re Matriculacion de " + str(alumno.apellido.title()) + " " + str(alumno.nombre.title()) + " ha sido creado con exito."
                            }
                            return JsonResponse(data)
                        else:
                            data = {
                                'error':True,
                                'resultado': " El email " + str(email_padre) + " no con corresponde con el dni del Padre."
                            }
                            return JsonResponse(data)
                    except Padre_madre.DoesNotExist:
                        data = {
                            'error':True,
                            'resultado': " No existe un Padre con ese dni."
                        }
                        return JsonResponse(data)
            except Alumno.DoesNotExist:
                data = {
                    'error':True,
                    'resultado': " No existe un Alumno con ese dni."
                }
                return JsonResponse(data)
        else:
            data = {
                'error':True,
                'resultado': str(re_matricular_form.errors)
            }
        return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

def cambiar_curso(request):
    if request.method == "POST":
        dni_alumno = request.POST['dni_alumno']
        id_curso = request.POST['id_curso']
        alumno = Alumno.objects.get(dni=dni_alumno)
        curso = Curso.objects.get(id=id_curso)
        alumno_C = Matriculacion.objects.get(alumno=alumno)
        alumno_C.curso = curso
        subject = "Curso de " + str(alumno.nombre.title()) + " modificado."
        secretaria = user_Trabajador.objects.get(user=request.user)
        message = " En el dia de la fecha la Secretaria " + str(secretaria.trabajador.apellido_t) + " " + str(secretaria.trabajador.nombre_t) + " ha cambiado el curso al que asiste su hijo/a " + str(alumno.nombre) + " a " + str(alumno_C.curso) + "."
        email_from = settings.EMAIL_HOST_USER

        familiares = Familia.objects.filter(alumno=alumno, habilitado=True)

        for familiar in familiares:
            recipient_list = [familiar.padre_madre.email]
            send_mail(subject, message, email_from, recipient_list)

        alumno_C.save()
        data = {
            'resultado': " El Alumno " + alumno.nombre.title() + " " + alumno.apellido.title() + " ahora asiste a " + str(alumno_C.curso)
        }
        return JsonResponse(data)

#Funcion para cambiar la password del usuario.
def cambiar_password(request):
    if request.method == "POST":
        form = get_Password(request.POST)
        if form.is_valid():
            print ("es valido")
            email = form.cleaned_data['email']
            dni = form.cleaned_data['dni']
            try:
                trabajador = Trabajador.objects.get(dni_t=dni)
                try:
                    trabajador = Trabajador.objects.get(email_t=email)
                    user_T = user_Trabajador.objects.get(trabajador=trabajador)
                    new_pass = trabajador.create_pass_user()
                    subject = "Recuperar Contraseña"
                    message = "El usuario " + str(user_T.user.username) + " utilizara la siguiente contraseña " + str(new_pass)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [trabajador.email_t]
                    send_mail( subject, message, email_from, recipient_list)
                    userd = User.objects.get(username=user_T.user.username)
                    userd.set_password(new_pass)
                    userd.save()
                    data = {
                        'resultado': " Clave cambiada con exito.",
                        'error':False
                    }
                    return JsonResponse(data)
                except Trabajador.DoesNotExist:
                    data = {
                        'resultado': " No existe un Trabajador con esta direccion de Email.",
                        'error':True
                    }
                    return JsonResponse(data)
            except Trabajador.DoesNotExist:
                    data = {
                        'resultado': " No existe un Trabajador con este Dni.",
                        'error':True
                    }
                    return JsonResponse(data)
        else:
            print (form.errors)
            aux = form.errors
            data = {
                'resultado': str(form.errors),
                'error':True
            }
            return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

def aplicar_cambios_alumno(request):
    if request.method == 'POST':
        alumno_form = Modificar_Alumno_Form(request.POST)
        dni_alumno = request.POST['dni']
        if alumno_form.is_valid():
            alumno = Alumno.objects.get(dni=dni_alumno)
            nombre = alumno_form.cleaned_data['nombre']
            apellido = alumno_form.cleaned_data['apellido']
            nuevo_lugar_nacimiento = alumno_form.cleaned_data['lugar_nacimiento']
            nueva_fecha_nacimiento = alumno_form.cleaned_data['fecha_nacimiento']
            nuevo_domicilio = alumno_form.cleaned_data['domicilio']
            nuevo_email = alumno_form.cleaned_data['email']
            nuevo_sexo = alumno_form.cleaned_data['sexo']
            nuevo_telefono_casa = alumno_form.cleaned_data['telefono_casa']
            nuevo_telefono_padre = alumno_form.cleaned_data['telefono_padre']
            nuevo_telefono_madre = alumno_form.cleaned_data['telefono_madre']
            nuevo_telefono_familiar = alumno_form.cleaned_data['telefono_familiar']
            nuevo_telefono_vecino = alumno_form.cleaned_data['telefono_vecino']
            nueva_enfermedad_relevante = alumno_form.cleaned_data['enfermedad_relevante']
            nuevo_con_quien_vive = alumno_form.cleaned_data['con_quien_vive']
            nuevo_quien_lo_trae = alumno_form.cleaned_data['quien_lo_trae']
            nuevo_telefono_que_lo_trae = alumno_form.cleaned_data['telefono_que_lo_trae']

            nuevo_nombre = nombre.lower()
            nuevo_apellido = apellido.lower()

            subject = "Informacion de " + str(alumno.nombre.title()) + " modificada."

            secretaria = user_Trabajador.objects.get(user=request.user)

            message = "En el dia de la fecha la secretaria " + str(secretaria.trabajador.apellido_t.title()) + " " + str(secretaria.trabajador.nombre_t.title()) + " ha realizado cambios en el perfil de " + str(alumno.nombre.title()) + "."
            email_from = settings.EMAIL_HOST_USER

            familiares = Familia.objects.filter(alumno=alumno, habilitado=True)

            for familiar in familiares:
                recipient_list = [familiar.padre_madre.email]
                send_mail(subject, message, email_from, recipient_list)

            alumno.nombre, alumno.apellido, alumno.lugar_nacimiento, alumno.fecha_nacimiento, alumno.domicilio, alumno.email, alumno.sexo, alumno.telefono_casa, alumno.telefono_padre, alumno.telefono_madre, alumno.telefono_familiar, alumno.telefono_vecino, alumno.enfermedad_relevante, alumno.con_quien_vive, alumno.quien_lo_trae, alumno.telefono_que_lo_trae  = nuevo_nombre, nuevo_apellido, nuevo_lugar_nacimiento, nueva_fecha_nacimiento, nuevo_domicilio, nuevo_email, nuevo_sexo, nuevo_telefono_casa, nuevo_telefono_padre, nuevo_telefono_madre, nuevo_telefono_familiar, nuevo_telefono_vecino, nueva_enfermedad_relevante, nuevo_con_quien_vive, nuevo_quien_lo_trae, nuevo_telefono_que_lo_trae

            alumno.save()
            data = {
                'error':False,
                'resultado': " Los datos de " + alumno.nombre.title() + " han sido modificados."
            }
            return JsonResponse(data)
        else:
            errores = str(alumno_form.errors)
            print (errores)
            data = {
                'error':True,
                'resultado':errores
            }
            return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

def modificar_curso(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    alumno_C = Matriculacion.objects.get(alumno=alumno)
    curso_actual = alumno_C.curso
    todos_los_cursos = Curso.objects.all().order_by("aNo").exclude(id=curso_actual.id)
    return render(request, 'cambiar_curso.html', {'alumno':alumno, 'todos_los_cursos':todos_los_cursos, 'curso_actual':curso_actual})

"""
==================
Crear y Modificar.
==================
"""

@user_passes_test(check_Secretaria)
def aceptar_matriculacion(request):
    if request.method == 'POST':
        dni_alumno = request.POST['dni_alumno']
        print (dni_alumno)
        selected_curso = request.POST['select_curso']
        print (selected_curso)
        curso = Curso.objects.get(id=selected_curso)
        alumno = Alumno.objects.get(dni=dni_alumno)
        matriculacion = Matriculacion.objects.get(alumno=alumno)
        matriculacion.matriculado = "Si"
        matriculacion.curso = curso
        matriculacion.save()
        familiares = Familia.objects.filter(alumno=alumno, habilitado=True)
        subject = "Pedido de Matriculacion de " + str(alumno.apellido.title()) + " " + str(alumno.nombre.title()) + "."
        secretaria = user_Trabajador.objects.get(user=request.user)
        message = "Se le notifica que la Secretaria " + secretaria.trabajador.apellido_t.title() + " " + secretaria.trabajador.nombre_t.title() + " ha aceptado el pedido de Matriculacion de su hijo/a " + alumno.apellido.title() + " " + alumno.nombre.title() + ", el cual ahora asistira a " + str(matriculacion.curso) + "."
        email_from = settings.EMAIL_HOST_USER
        for familiar in familiares:
            recipient_list = [familiar.padre_madre.email]
            send_mail( subject, message, email_from, recipient_list)
        data = {
            'resultado': "El alumno " + str(alumno.apellido.title()) + " " + str(alumno.nombre.title()) + " asiste al curso " + str(matriculacion.curso),
            'error': False
        }
        return JsonResponse(data, safe=True)
    return HttpResponse("Solo podes entrar por POST")

"""
======
Login.
======
"""

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        print (username)
        print (password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            data = {
                'error': False
            }
        else:
            data = {
            'estado': " Nombre de usuario o contraseña no son correctos",
            'error': True
            }
    return JsonResponse(data, safe=True)


"""
===========
Desvincular
===========
"""

def desvincular_transportista(request):
    if request.method == 'POST':
        dni_alumno = request.POST['dni_alumno']
        dni_transportista = request.POST['dni_transportista']
        print (dni_transportista)
        alumno = Alumno.objects.get(dni=dni_alumno)
        transportista = Transportista.objects.get(dni=dni_transportista)
        medio = usa_Transporte.objects.get(alumno=alumno, transportista=transportista)
        medio.habilitado = False
        medio.save()
        return redirect ('transportistas_del_alumno', "perfil", dni_alumno)
    return HttpResponse("Solo por acceder por Post")

def desvincular_obra_social(request):
    if request.method == 'POST':
        dni_alumno = request.POST['dni_alumno']
        id_obra_social = request.POST['id_obra_social']
        alumno = Alumno.objects.get(dni=dni_alumno)
        obra_social = Obra_Social.objects.get(pk=id_obra_social)
        medio = usa_Obra_Social.objects.get(alumno=alumno, obra_social=obra_social)
        medio.habilitado = False
        medio.save()
        return redirect ('obras_sociales_del_alumno',"perfil", dni_alumno)
    return HttpResponse("Solo por acceder por Post")

def desvincular_familiar(request):
    if request.method == 'POST':
        dni_alumno = request.POST['dni_alumno']
        dni_padre = request.POST['dni_padre']
        alumno = Alumno.objects.get(dni=dni_alumno)
        padre = Padre_madre.objects.get(dni=dni_padre)
        medio = Familia.objects.get(alumno=alumno, padre_madre=padre)
        medio.habilitado = False
        medio.save()
        return redirect ('padres_del_alumno', "perfil", dni_alumno)
    return HttpResponse("Solo por acceder por Post")

def desvincular_autorizado(request):
    if request.method == 'POST':
        dni_alumno = request.POST['dni_alumno']
        dni_autorizado = request.POST['dni_autorizado']
        alumno = Alumno.objects.get(dni=dni_alumno)
        autorizado = Autorizado.objects.get(dni=dni_autorizado)
        medio = alumno_Autorizado.objects.get(alumno=alumno, autorizado=autorizado)
        medio.habilitado = False
        medio.save()
        return redirect ('autorizados_del_alumno',"perfil", dni_alumno)
    return HttpResponse("Solo por acceder por Post")
