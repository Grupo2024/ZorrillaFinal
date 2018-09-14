from django.core.management.base import BaseCommand, CommandError
from institucion.models import *
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
	def index(self, *args, **options):
	    user_secretaria = User.objects.create_user('secretaria', 'mumi@gmail.com', 'hola1234')
	    grupo_secretaria, created = Group.objects.get_or_create(name='grupo_secretaria')
	    user_profesor = User.objects.create_user('profesor', 'pancho@gmail.com', 'hola1234')
	    grupo_profesor, created = Group.objects.get_or_create(name='grupo_profesor')
	    user_director = User.objects.create_user('director', 'arce@gmail.com', 'hola1234')
	    grupo_director, created = Group.objects.get_or_create(name='grupo_director')

	    #new_group, created = Group.objects.get_or_create(name='new_group')

	    a = Secretaria(nombre_t="a", apellido_t="a", dni_t=11111111, lugar_nacimiento_t="a", 
	    fecha_nacimiento_t=1980-1-1, domicilio_t="a", email_t="mumi@gmail.com", sexo_t="Mujer", 
	    telefono_particular=1, telefono_laboral=1, telefono_familiar=1, datos_familiares_cargo="a",
	    fecha_inicio_actividad=2017-1-1, antecedentes_laborales="a", estudios_cursados="a") 

	    b = Profesor(nombre_t="b", apellido_t="b", dni_t=22222222, lugar_nacimiento_t="b", 
	    fecha_nacimiento_t=1980-2-2, domicilio_t="b", email_t="pancho@gmail.com", sexo_t="Hombre", 
	    telefono_particular=2, telefono_laboral=2, telefono_familiar=2, datos_familiares_cargo="b",
	    fecha_inicio_actividad=2017-2-2, antecedentes_laborales="b", estudios_cursados="b")
	    
	    a = Director(nombre_t="c", apellido_t="c", dni_t=33333333, lugar_nacimiento_t="c", 
	    fecha_nacimiento_t=1980-3-3, domicilio_t="c", email_t="arce@gmail.com", sexo_t="Hombre", 
	    telefono_particular=3, telefono_laboral=3, telefono_familiar=3, datos_familiares_cargo="c",
	    fecha_inicio_actividad=2017-3-3, antecedentes_laborales="c", estudios_cursados="c")

        secretaria_aux = user_Secretaria(user=user_secretaria,secretaria_referenciada=a)
        profesor_aux = user_profesor(user=user_profesor,profesor_referenciado=b)
        director_aux = user_Director(user=user_director,director_referenciado=c)
        secretaria_aux.save()
        profesor_aux.save()
        director_aux.save()
        print "Funciona"
