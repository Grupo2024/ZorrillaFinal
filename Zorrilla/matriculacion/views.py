# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from .creation import *
from .test_model import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from biblioteca.decorators import *

# Create your views here.

def daddy():
    cant_profesores = Profesor.objects.all().count()
    if cant_profesores == 0:
        password = "hola1234"
        user_secretaria = User.objects.create_user(username="secretaria", password=password)
        grupo_secretaria, created = Group.objects.get_or_create(name='Secretaria')
        user_profesor = User.objects.create_user(username="profesor", password=password)
        grupo_profesor, created = Group.objects.get_or_create(name='Profesor')
        user_director = User.objects.create_user(username="director", password=password)
        grupo_director, created = Group.objects.get_or_create(name='Director')
        grupo_secretaria = Group.objects.get(name='Secretaria') 
        grupo_secretaria.user_set.add(user_secretaria)
        my_group2 = Group.objects.get(name='Profesor') 
        my_group2.user_set.add(user_profesor)
        my_group3 = Group.objects.get(name='Director') 
        my_group3.user_set.add(user_director)
        #new_group, created = Group.objects.get_or_create(name='new_group')
        a = Secretaria(nombre_t="a", apellido_t="a", dni_t=11111111, lugar_nacimiento_t="a", 
        fecha_nacimiento_t="1980-01-01", domicilio_t="a", email_t="mumi@gmail.com", sexo_t="Mujer", 
        telefono_particular=1, telefono_laboral=1, telefono_familiar=1, datos_familiares_cargo="a",
        fecha_inicio_actividad="2018-03-01", antecedentes_laborales="a", estudios_cursados="a") 
        b = Profesor(nombre_t="b", apellido_t="b", dni_t=22222222, lugar_nacimiento_t="b", 
        fecha_nacimiento_t="1980-02-02", domicilio_t="b", email_t="pancho@gmail.com", sexo_t="Hombre", 
        telefono_particular=2, telefono_laboral=2, telefono_familiar=2, datos_familiares_cargo="b",
        fecha_inicio_actividad="2018-02-02", antecedentes_laborales="b", estudios_cursados="b")
        c = Director(nombre_t="c", apellido_t="c", dni_t=33333333, lugar_nacimiento_t="c", 
        fecha_nacimiento_t="1980-03-03", domicilio_t="c", email_t="arce@gmail.com", sexo_t="dudoso", 
        telefono_particular=3, telefono_laboral=3, telefono_familiar=3, datos_familiares_cargo="c",
        fecha_inicio_actividad="2018-03-03", antecedentes_laborales="c", estudios_cursados="c")
        a.save()
        b.save()
        c.save()
        secretaria_aux = user_Secretaria(user=user_secretaria,secretaria_referenciada=a)
        profesor_aux = user_Docente(user=user_profesor,docente_referenciado=b)
        director_aux = user_Director(user=user_director,director_referenciado=c)
        secretaria_aux.save()
        profesor_aux.save()
        director_aux.save()
        return "Creados"
    else:
        return "Ya estan creados"

"""
===================
Levantar Templates.
===================
"""

def logIn(request):
    return render(request, 'docentes_login.html')

def index(request):
    daddy()
    return render(request, 'index.html')

@login_required
def logout_me_out(request):
    auth.logout(request)
    return redirect ('index')
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

#Levantar Template para cargar Transportista.
def form_transportista(request):
    form_transportista = TransportistaForm()
    return render (request, 'Transportista/crear_transportista.html', {'form_transportista':form_transportista})

#Levantar el Form para cambiar la password.
def template_get_pass(request):
    print ("entra")
    form = get_Password()
    return render (request, 'new_password/my_info.html', {'form':form})

#Levantar el Form para cargar al Padre.
def cargar_padre(request, dni_alumno):
    padre_form = PadreForm()
    return render(request, 'Padre_madre/crear_padre_madre.html', {'padre_form':padre_form, 'dni_alumno':dni_alumno})


def modificar_alumno(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    alumno_form = Modificar_Alumno_Form(initial={'nombre':alumno.nombre, 'apellido':alumno.apellido,'lugar_nacimiento':alumno.lugar_nacimiento, 'fecha_nacimiento':alumno.fecha_nacimiento, 'domicilio':alumno.domicilio, 'email':alumno.email, 'sexo':alumno.sexo, 'telefono_casa':alumno.telefono_casa, 'telefono_padre':alumno.telefono_padre, 'telefono_madre':alumno.telefono_madre, 'telefono_familiar':alumno.telefono_familiar, 'telefono_vecino':alumno.telefono_vecino, 'enfermedad_relevante':alumno.enfermedad_relevante, 'con_quien_vive':alumno.con_quien_vive, 'quien_lo_trae':alumno.quien_lo_trae, 'telefono_que_lo_trae':alumno.telefono_que_lo_trae})
    return render(request, 'modificar_alumno.html', {'alumno_form':alumno_form, 'dni_alumno':dni_alumno})

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
        padre_form = PadreForm()
        return render(request, 'Padre_madre/cargar_padre.html', {'padre_form':padre_form, 'datos_alumno':datos_alumno})
    else:
        aux = alumno_form.errors
        return HttpResponse(str(aux))


#Funcoin que crea al Padre.
def crear_padre(request):
    padre_form = PadreForm(request.POST)
    dni_alumno = request.POST['dni_alumno']
    alumno = Alumno.objects.get(dni=dni_alumno)
    if padre_form.is_valid():
        print ("es valido")
        padre_form.save()
        dni_padre = padre_form.cleaned_data['dni']
        padre = Padre_madre.objects.get(dni=dni_padre)
        print (padre)
        secretaria = user_Secretaria.objects.get(user=request.user)
        familia = Familia(alumno=alumno, padre_madre=padre, secretaria=secretaria.secretaria_referenciada)
        familia.save()
        new_Matriculacion = Matriculacion(alumno=alumno, matriculado="No")
        new_Matriculacion.save()
        resultado = "Los pedidos de Matriculacion de " + str(padre.apellido) + " " + str(padre.nombre) + " y de " + str(alumno.apellido) + " " + str(alumno.nombre) + " han sido creados con exito."
        data = {
            'error': False,
            'resultado':resultado
        }
        return JsonResponse(data)
    else:
        resultado = str(padre_form.errors)
        data = {
            'error':True,
            'resultado':resultado
        }
        return JsonResponse(data)
    
def crear_padre_madre(request):
    padre_form = PadreForm(request.POST)
    if padre_form.is_valid():
        print "Es valido"
        padre_form.save()
        dni_padre = padre_form.cleaned_data['dni']
        padre = Padre_madre.objects.get(dni=dni_padre)
        resultado = "El Padre " + str(padre.apellido) + " " + str(padre.nombre) + " ha sido creado con exito."
        data = {
            'error':False,
            'resultado':resultado
        }
    else:
        print "No es valido"
        resultado = str(padre_form.errors)
        print resultado
        data = {
            'error':True,
            'resultado':resultado
        }
        return JsonResponse(data)

#Funcion que Crea al Transportista.
def crear_transportista(request):
    print ("crear transportista")
    if request.method == 'POST':
        form_transportista = TransportistaForm(request.POST)
        if form_transportista.is_valid():
            form_transportista.save()
            nombre = form_transportista.cleaned_data['nombre']
            apellido = form_transportista.cleaned_data['apellido']
            data = {
                'error':False,
                'resultado': 'El transportista ' + str(nombre) + ' ' + str(apellido) + ' ha sido cargado con exito.'
            }
            return JsonResponse(data)
        else:
            data = {
                'error':True,
                'resultado':str(form_transportista.errors)
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
        print dni
        print dni_padre
        padre = Padre_madre.objects.get(dni=dni_padre)
        secretaria = user_Secretaria.objects.get(user=request.user)
        familia = Familia(alumno=alumno, padre_madre=padre, secretaria=secretaria.secretaria_referenciada)
        familia.save()
        familia.save()
        data = {
            'resultado': 'Padre asignado con exito.'
        }
        return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")

"""
========================================
Traer Todas las instancias de un modelo.
========================================
"""

#Traer Todos los Transnportistas.
def todos_los_transportistas(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    transportistas_ya_asignados = usa_Transporte.objects.filter(alumno=alumno)
    lista = []
    for a in transportistas_ya_asignados:
        lista.append(a.transportista.dni)
    transportistas = Transportista.objects.exclude(dni__in=lista)
    return render(request, 'Transportista/todos_los_transportistas.html',{'transportistas':transportistas, 'dni_alumno':dni_alumno})

#Traer Todos los Padres/Madre.
def todos_los_padres(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    padres_ya_asignados = Familia.objects.filter(alumno=alumno)
    lista = []
    for a in padres_ya_asignados:
        lista.append(a.padre_madre.dni)
    padre = Padre_madre.objects.exclude(dni__in=lista)
    padres = Padre_madre.objects.all()
    print (padres)
    return render(request,'Padre_madre/todos_los_padres.html', {'todos_los_padres':padre, 'dni_alumno':dni_alumno})

#Traer Todos las Matriculaciones con estado 'No' y 'Re'.
@user_passes_test(check_Secretaria)
def traer_pedidos(request):
    matriculaciones = Matriculacion.objects.filter(matriculado="No")
    re_matriculaciones = Matriculacion.objects.filter(matriculado = "Re")
    return render(request, 'pedidos.html', {'matriculaciones':matriculaciones, 're_matricular':re_matriculaciones})

def padres_del_alumno(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    familia = Familia.objects.filter(alumno=alumno)
    return render(request, 'Padre_madre/padres_del_alumno.html', {'familiares':familia, 'alumno':alumno})

def transportistas_del_alumno(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    transportistas = usa_Transporte.objects.filter(alumno=alumno)
    return render(request, 'Transportista/transportistas_del_alumno.html', {'transportistas':transportistas, 'alumno':alumno})

def obras_sociales_del_alumno(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    obras_sociales = usa_Obra_Social.objects.filter(alumno=alumno)
    return render(request, 'Obra_Social/obras_sociales_del_alumno.html', {'obras_sociales':obras_sociales, 'alumno':alumno})

"""
===================================
Mostrar los datos de una instancia.
===================================
"""

#Funcion que Trae los datos del Transportista elegido previamente
def datos_transportista(request, dni_transportista):
    transportista = Transportista.objects.get(dni=dni_transportista)
    return render(request, 'Transportista/datos_transportista.html', {'transportista':transportista})

#Funcion que Trae los datos del Padre elegido previamente
def datos_padre(request, dni_padre):
    padre = Padre_madre.objects.get(dni=dni_padre)
    return render(request, 'Padre_madre/datos_padre.html', {'padre':padre})

#Funcion que Trae los datos del Alumno elegido previamente
@login_required
def datos_alumno(request, id_alumno):
    alumno = Alumno.objects.get(dni=id_alumno)
    transportistas = usa_Transporte.objects.filter(alumno=alumno)
    if not transportistas:
        alumno.transporte = "No"
    else:
        alumno.transporte = "Si"
    #matriculado = Matriculacion.objects.get(alumno=alumno, matriculado="Si")
    try:
        matriculado = Matriculacion.objects.get(alumno=alumno, matriculado="Si")
        alumno.matriculado = "Si"
    except Matriculacion.DoesNotExist:
        alumno.matriculado = "No"
    obras_sociales = usa_Obra_Social.objects.filter(alumno=alumno)
    if not obras_sociales:
        alumno.obra_social = "No"
    else:
        alumno.obra_social = "Si"
    familiares = Familia.objects.filter(alumno=alumno)
    return render(request, 'perfilAlumno.html', {'alumno':alumno, 'familiares':familiares})

#Funcion que Trae los Familiares, Transportistas del Alumno y los Cursos.
def get_Secciones(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    familiares = Familia.objects.filter(alumno=alumno).order_by("padre_madre__apellido", "padre_madre__nombre")
    transportistas = usa_Transporte.objects.filter(alumno=alumno)
    cursos = Curso.objects.all()
    return render(request, 'matricular.html', {'familiares':familiares, 'alumno':alumno, 'cursos':cursos, 'transportistas':transportistas})

#Funcion que Trae los Familiares, Transportistas, Curso Actual del Alumno y los Cursos.
def re_matricular(request, dni_alumno):
    alumno = Alumno.objects.get(dni=dni_alumno)
    familiares = Familia.objects.filter(alumno=alumno).order_by("padre_madre__apellido", "padre_madre__nombre")
    transportistas = usa_Transporte.objects.filter(alumno=alumno)
    curso2 = alumno_Curso.objects.get(alumno=alumno)
    curso = curso2.curso
    cursos = Curso.objects.all()
    recomendacion = Curso.objects.get(aNo=curso.aNo+1)
    return render(request, 're_matricular.html', {'familiares':familiares, 'alumno':alumno, 'cursos':cursos, 'transportistas':transportistas, 'curso':curso, 'recomendacion':recomendacion})

"""
==========
Modificar.
==========
"""

#Funcion para cambiar la password del usuario.
def cambiar_password(request):
    if request.method == "POST":
        form = get_Password(request.POST)
        if form.is_valid():
            print ("es valido")
            email = form.cleaned_data['email']
            dni = form.cleaned_data['dni']
            try:
                profesor = Profesor.objects.get(email_t=email)
                try:
                    profesor = Profesor.objects.get(dni_t=dni)
                    userD = user_Docente.objects.get(docente_referenciado=profesor)
                    print (userD.user.username)
                    new_pass = new_Password(profesor.dni_t)
                    subject = "Recuperar Contraseña"
                    message = "El usuario " + str(userD.user.username) + " utilizara la siguiente contraseña " + str(new_pass)
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [profesor.email_t]
                    send_mail( subject, message, email_from, recipient_list)
                    print ("funciona")
                    userd = User.objects.get(username=userD.user.username)
                    print ("Vieja Pass" + str(userd.password))
                    userd.set_password(new_pass)
                    userd.save()
                    print ("nueva pass" + str(userd.password))
                    data = {
                        'resultado': "Clave cambiada con exito.",
                        'error':False
                    }
                    return JsonResponse(data)
                except Profesor.DoesNotExist:
                    data = {
                        'resultado': "No existe un profesor con esta direccion de Email.",
                        'error':True
                    }
                    return JsonResponse(data)
            except Profesor.DoesNotExist:
                    data = {
                        'resultado': "No existe un profesor con ese Dni.",
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
        dni_alumno = request.POST['dni_alumno']
        if alumno_form.is_valid():
            print "Es valido"
            alumno = Alumno.objects.get(dni=dni_alumno)
            nuevo_nombre = alumno_form.cleaned_data['nombre']
            nuevo_apellido = alumno_form.cleaned_data['apellido']
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

            alumno.nombre, alumno.apellido, alumno.lugar_nacimiento, alumno.fecha_nacimiento, alumno.domicilio, alumno.email, alumno.sexo, alumno.telefono_casa, alumno.telefono_padre, alumno.telefono_madre, alumno.telefono_familiar, alumno.telefono_vecino, alumno.enfermedad_relevante, alumno.con_quien_vive, alumno.quien_lo_trae, alumno.telefono_que_lo_trae  = nuevo_nombre, nuevo_apellido, nuevo_lugar_nacimiento, nueva_fecha_nacimiento, nuevo_domicilio, nuevo_email, nuevo_sexo, nuevo_telefono_casa, nuevo_telefono_padre, nuevo_telefono_madre, nuevo_telefono_familiar, nuevo_telefono_vecino, nueva_enfermedad_relevante, nuevo_con_quien_vive, nuevo_quien_lo_trae, nuevo_telefono_que_lo_trae
            alumno.save()
            data = {
                'resultado': "Los datos de " + alumno.nombre + " han sido modificados."
            }
            return JsonResponse(data)
        else:
            errores = str(alumno_form.errors)
            print errores
            data = {
                'resultado':errores
            }
            return JsonResponse(data)
    return HttpResponse("Solo podes acceder por Post")


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
        eleccion = alumno_Curso(alumno=alumno, curso=curso)
        eleccion.save()
        matriculacion = Matriculacion.objects.get(alumno=alumno)
        matriculacion.matriculado = "Si"
        matriculacion.save()
        data = {
            'resultado': "El alumno " + str(alumno.apellido) + " " + str(alumno.nombre) + " asiste al curso " + str(eleccion.curso),
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
            'estado': "nombre de usuario o contraseña no son correctos",
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
        medio.delete()
        return redirect ('transportistas_del_alumno', dni_alumno)
    return HttpResponse("Solo por acceder por Post")

def desvincular_obra_social(request):
    if request.method == 'POST':
        dni_alumno = request.POST['dni_alumno']
        id_obra_social = request.POST['id_obra_social']
        alumno = Alumno.objects.get(dni=dni_alumno)
        obra_social = Obra_Social.objects.get(pk=id_obra_social)
        medio = usa_Obra_Social.objects.get(alumno=alumno, obra_social=obra_social)
        medio.delete()
        return redirect ('obras_sociales_del_alumno', dni_alumno)
    return HttpResponse("Solo por acceder por Post")

def desvincular_familiar(request):
    if request.method == 'POST':
        dni_alumno = request.POST['dni_alumno']
        dni_padre = request.POST['dni_padre']
        alumno = Alumno.objects.get(dni=dni_alumno)
        padre = Padre_madre.objects.get(dni=dni_padre)
        medio = Familia.objects.get(alumno=alumno, padre_madre=padre)
        medio.delete()
        return redirect ('padres_del_alumno', dni_alumno)
    return HttpResponse("Solo por acceder por Post")
