# -*- coding: utf-8 -*-

# Generated by Django 1.11.2 on 2018-10-09 11:36

# Generated by Django 1.11.11 on 2018-10-09 14:42

from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='clave_Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_logIn', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('email_docente', models.EmailField(max_length=254, unique=True)),
                ('dni_docente', models.IntegerField(unique=True)),
                ('ingresado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.BooleanField(verbose_name='Clickea para seleccionar turno "Tarde"')),
                ('aNo', models.IntegerField(verbose_name='1,2,3,4...')),
                ('seccion', models.BooleanField(verbose_name='True = B o D, dependiendo de si es turno ma\xf1ana o tarde')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('nombre_t', models.CharField(max_length=40, verbose_name='Nombre del trabajador')),
                ('apellido_t', models.CharField(max_length=40, verbose_name='Apellido del trabajador')),
                ('dni_t', models.IntegerField(primary_key=True, serialize=False, verbose_name='Dni del trabajador')),
                ('lugar_nacimiento_t', models.CharField(blank=True, max_length=150, verbose_name='Lugar de Nacimiento')),
                ('fecha_nacimiento_t', models.DateField(blank=True, verbose_name='Fecha Nacimiento')),
                ('domicilio_t', models.CharField(blank=True, max_length=150, verbose_name='Domicilio del trabajador')),
                ('email_t', models.EmailField(max_length=70, verbose_name='Email del trabajador')),
                ('sexo_t', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6, verbose_name='Sexo')),
                ('telefono_particular', models.IntegerField(verbose_name='Telefono Personal del Trabajador')),
                ('telefono_laboral', models.IntegerField(verbose_name='Telefono Laboral del Trabajador')),
                ('telefono_familiar', models.IntegerField(verbose_name='Telefono de algun Familiar del Trabajador')),
                ('datos_familiares_cargo', models.TextField(max_length=300, verbose_name='Nombre y Apellido de familiar del Trabajador')),
                ('fecha_inicio_actividad', models.DateField(auto_now_add=True, verbose_name='Fecha de Inicio de Clases en el Colegio')),
                ('antecedentes_laborales', models.TextField(max_length=300, verbose_name='Datos de Trabajos Previos')),
                ('estudios_cursados', models.TextField(max_length=300, verbose_name='Estudios del Trabajador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('nombre_t', models.CharField(max_length=40, verbose_name='Nombre del trabajador')),
                ('apellido_t', models.CharField(max_length=40, verbose_name='Apellido del trabajador')),
                ('dni_t', models.IntegerField(primary_key=True, serialize=False, verbose_name='Dni del trabajador')),
                ('lugar_nacimiento_t', models.CharField(blank=True, max_length=150, verbose_name='Lugar de Nacimiento')),
                ('fecha_nacimiento_t', models.DateField(blank=True, verbose_name='Fecha Nacimiento')),
                ('domicilio_t', models.CharField(blank=True, max_length=150, verbose_name='Domicilio del trabajador')),
                ('email_t', models.EmailField(max_length=70, verbose_name='Email del trabajador')),
                ('sexo_t', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6, verbose_name='Sexo')),
                ('telefono_particular', models.IntegerField(verbose_name='Telefono Personal del Trabajador')),
                ('telefono_laboral', models.IntegerField(verbose_name='Telefono Laboral del Trabajador')),
                ('telefono_familiar', models.IntegerField(verbose_name='Telefono de algun Familiar del Trabajador')),
                ('datos_familiares_cargo', models.TextField(max_length=300, verbose_name='Nombre y Apellido de familiar del Trabajador')),
                ('fecha_inicio_actividad', models.DateField(auto_now_add=True, verbose_name='Fecha de Inicio de Clases en el Colegio')),
                ('antecedentes_laborales', models.TextField(max_length=300, verbose_name='Datos de Trabajos Previos')),
                ('estudios_cursados', models.TextField(max_length=300, verbose_name='Estudios del Trabajador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('nombre_t', models.CharField(max_length=40, verbose_name='Nombre del trabajador')),
                ('apellido_t', models.CharField(max_length=40, verbose_name='Apellido del trabajador')),
                ('dni_t', models.IntegerField(primary_key=True, serialize=False, verbose_name='Dni del trabajador')),
                ('lugar_nacimiento_t', models.CharField(blank=True, max_length=150, verbose_name='Lugar de Nacimiento')),
                ('fecha_nacimiento_t', models.DateField(blank=True, verbose_name='Fecha Nacimiento')),
                ('domicilio_t', models.CharField(blank=True, max_length=150, verbose_name='Domicilio del trabajador')),
                ('email_t', models.EmailField(max_length=70, verbose_name='Email del trabajador')),
                ('sexo_t', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6, verbose_name='Sexo')),
                ('telefono_particular', models.IntegerField(verbose_name='Telefono Personal del Trabajador')),
                ('telefono_laboral', models.IntegerField(verbose_name='Telefono Laboral del Trabajador')),
                ('telefono_familiar', models.IntegerField(verbose_name='Telefono de algun Familiar del Trabajador')),
                ('datos_familiares_cargo', models.TextField(max_length=300, verbose_name='Nombre y Apellido de familiar del Trabajador')),
                ('fecha_inicio_actividad', models.DateField(auto_now_add=True, verbose_name='Fecha de Inicio de Clases en el Colegio')),
                ('antecedentes_laborales', models.TextField(max_length=300, verbose_name='Datos de Trabajos Previos')),
                ('estudios_cursados', models.TextField(max_length=300, verbose_name='Estudios del Trabajador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='user_Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_referenciado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institucion.Director')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docente_referenciado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institucion.Profesor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_Secretaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretaria_referenciada', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institucion.Secretaria')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
