# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from matriculacion.models import *
import random

from django.contrib.auth.models import User

# Create your models here.

class clave_Docente(models.Model):
    clave_logIn = models.CharField(null=False, max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    email_docente = models.EmailField(null=False, unique=True)
    dni_docente = models.IntegerField(null=False, unique=True)
    ingresado = models.BooleanField(default=False)#False hasta que se ingrese el docente al sistema.
    
    def change(self):
        if self.ingresado:
            self.ingresado = False
            self.save()
            return self.ingresado
        else:
            self.ingresado = True
            self.save()
            return self.ingresado


# Create your models here.

class Trabajador(models.Model):
    
    HO = 'Hombre'
    MU = 'Mujer'
    PR = 'Profesor'
    SE = 'Secretaria'
    DI = 'Director'

    CARGO_CHOICES = (
        (PR , 'Profesor'),
        (SE , 'Secretaria'),
        (DI , 'Director')
    )
    
    GENERO_CHOICES = (
        (HO , 'Hombre'),
        (MU , 'Mujer'),
    )
    
    #Datos estandares del trabajador, estos van a ser heredados x cualquier profesor, director o secretaria
    nombre_t = models.CharField('Nombre del trabajador', max_length=40)
    apellido_t = models.CharField('Apellido del trabajador', max_length=40)
    dni_t = models.IntegerField('Dni del trabajador', primary_key=True)
    lugar_nacimiento_t = models.CharField('Lugar de Nacimiento', max_length=150)
    fecha_nacimiento_t = models.DateField('Fecha Nacimiento', blank=True)
    domicilio_t = models.CharField('Domicilio del trabajador', max_length=150, blank=True)
    email_t = models.EmailField('Email del trabajador', max_length=70, unique=True)
    sexo_t = models.CharField('Sexo', max_length=6, choices=GENERO_CHOICES)
    cargo_t = models.CharField('Cargo', max_length=10, choices=CARGO_CHOICES)
    telefono_particular = models.IntegerField('Telefono Personal del Trabajador')
    telefono_laboral = models.IntegerField('Telefono Laboral del Trabajador')
    telefono_familiar = models.IntegerField('Telefono de algun Familiar del Trabajador')
    datos_familiares_cargo = models.TextField('Nombre y Apellido de familiar del Trabajador', max_length=300)
    fecha_inicio_actividad = models.DateField('Fecha de Inicio de Clases en el Colegio', auto_now_add=True)
    antecedentes_laborales = models.TextField('Datos de Trabajos Previos', max_length=300)
    estudios_cursados = models.TextField('Estudios del Trabajador', max_length=300)

    def create_pass_user(self):
        name_f = ""
        cantidad = 0
        r = random.randint(1111,9999)
        for a in self.nombre_t:
            cantidad = cantidad + 1
            if cantidad == 1:
                name_f = a
                break
            else:
                pass
        password = name_f + str(r) + self.apellido_t
        return password

    def create_username(self):
        name_f = ""
        cantidad = 0
        dni_t = int(str(self.dni_t)[:4])
        for a in self.nombre_t:
            cantidad = cantidad + 1
            if cantidad == 1:
                name_f = a
                break
            else:
                pass

        username = name_f + str(dni_t) + self.apellido_t
        return username

    def __str__(self):
        return 'Trabajador: {} {}| dni: {}| sexo: {} puesto: {}'.format(self.nombre_t,
         self.apellido_t, self.dni_t, self.sexo_t, self.cargo_t)


class Curso(models.Model):
    hora = models.BooleanField('Clickea para seleccionar turno "Tarde"', null=False)
    aNo = models.IntegerField('1ero, 2do, etc...')
    seccion = models.BooleanField('True = B o D, dependiendo de si es turno mañana o tarde', null=False)

    def que_turno(self):
        aux = 'Maniana'
        if (self.hora == True):
            aux = 'Tarde'
            return aux
        else:
            return aux

    def que_seccion(self):
        if (self.hora == True):
            aux = 'C'
            if (self.seccion == True):
                aux = 'D'
                return aux
            else:
                return aux
        else:
            aux = 'A'
            if (self.seccion == True):
                aux = 'B'
                return aux
            else:
                return aux
            
    # HORA: TRUE, SECCION TRUE: --- D
    # HORA: FALSE, SECCION TRUE: ---- B
    # HORA: TRUE, SECCION FALSE: ---- C
    # HORA: FALSE, SECCION FALSE: ----- A

    def new_turno(self):
        if self.hora:
            self.turno = "Tarde"
        else:
            self.turno = "Maniana"
        return self.turno

    def pasar(self):
        siguiente = Curso.objects.get(aNo=self.aNo+1)
        opcion = str(siguiente.aNo) + "-" + str(siguiente.seccion)
        print (siguiente)
        return "nada"

    def __str__(self):
        return '{}-{}' .format(self.aNo, self.que_seccion())

class user_Trabajador(models.Model):
    user = models.OneToOneField(User, unique=True)
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return 'El usuario {} pertenece al trabajador: {}'.format(self.user, self.trabajador.nombre_t, self.trabajador.apellido_t)

