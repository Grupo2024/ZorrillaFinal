# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class InstitucionConfig(AppConfig):
    name = 'institucion'

    def ready(self):
        from institucion.models import *
        from django.contrib.auth.models import User, Group

        user_secretaria, created = User.objects.get_or_create(username='secretaria', 
        email='mumi@gmail.com', password='hola1234')
        grupo_secretaria, created = Group.objects.get_or_create(name='Secretaria')
        user_profesor, created = User.objects.get_or_create(username='profesor', 
        email='pancho@gmail.com', password='hola1234')
        grupo_profesor, created = Group.objects.get_or_create(name='Profesor')
        user_director, created = User.objects.get_or_create(username='director', 
        email='arce@gmail.com', password='hola1234')
        grupo_director, created = Group.objects.get_or_create(name='Director')

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
        
        print "Funciona"


