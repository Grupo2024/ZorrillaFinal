# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='clave_Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_logIn', models.CharField(max_length=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('email_docente', models.EmailField(max_length=254)),
                ('dni_docente', models.IntegerField()),
                ('ingresado', models.BooleanField(default=False)),
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
                ('email_t', models.EmailField(blank=True, max_length=70, verbose_name='Email del trabajador')),
                ('sexo_t', models.BooleanField(verbose_name='Sexo del trabajador(True = Hombre)')),
                ('telefono_particular', models.IntegerField(verbose_name='Telefono Personal del Trabajador')),
                ('telefono_laboral', models.IntegerField(verbose_name='Telefono Laboral del Trabajador')),
                ('telefono_familiar', models.IntegerField(verbose_name='Telefono de algun Familiar del Trabajador')),
                ('datos_familiares_cargo', models.TextField(max_length=300, verbose_name='Nombre y Apellido de familiar del Trabajador')),
                ('fecha_inicio_actividad', models.DateField(verbose_name='Fecha de Inicio de Clases en el Colegio')),
                ('antecedentes_laborales', models.TextField(max_length=300, verbose_name='Datos de Trabajos Previos')),
                ('antiguedad_en_empresa', models.DateField(verbose_name='Antiguedad en la Empresa')),
                ('estudios_cursados', models.TextField(max_length=300, verbose_name='Estudios del Trabajador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aNo', models.CharField(max_length=5, verbose_name='1ero, 2do, etc...')),
            ],
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
                ('email_t', models.EmailField(blank=True, max_length=70, verbose_name='Email del trabajador')),
                ('sexo_t', models.BooleanField(verbose_name='Sexo del trabajador(True = Hombre)')),
                ('telefono_particular', models.IntegerField(verbose_name='Telefono Personal del Trabajador')),
                ('telefono_laboral', models.IntegerField(verbose_name='Telefono Laboral del Trabajador')),
                ('telefono_familiar', models.IntegerField(verbose_name='Telefono de algun Familiar del Trabajador')),
                ('datos_familiares_cargo', models.TextField(max_length=300, verbose_name='Nombre y Apellido de familiar del Trabajador')),
                ('fecha_inicio_actividad', models.DateField(verbose_name='Fecha de Inicio de Clases en el Colegio')),
                ('antecedentes_laborales', models.TextField(max_length=300, verbose_name='Datos de Trabajos Previos')),
                ('antiguedad_en_empresa', models.DateField(verbose_name='Antiguedad en la Empresa')),
                ('estudios_cursados', models.TextField(max_length=300, verbose_name='Estudios del Trabajador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=1, verbose_name='A-B-C-D')),
                ('grado_asignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.Grado')),
            ],
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
                ('email_t', models.EmailField(blank=True, max_length=70, verbose_name='Email del trabajador')),
                ('sexo_t', models.BooleanField(verbose_name='Sexo del trabajador(True = Hombre)')),
                ('telefono_particular', models.IntegerField(verbose_name='Telefono Personal del Trabajador')),
                ('telefono_laboral', models.IntegerField(verbose_name='Telefono Laboral del Trabajador')),
                ('telefono_familiar', models.IntegerField(verbose_name='Telefono de algun Familiar del Trabajador')),
                ('datos_familiares_cargo', models.TextField(max_length=300, verbose_name='Nombre y Apellido de familiar del Trabajador')),
                ('fecha_inicio_actividad', models.DateField(verbose_name='Fecha de Inicio de Clases en el Colegio')),
                ('antecedentes_laborales', models.TextField(max_length=300, verbose_name='Datos de Trabajos Previos')),
                ('antiguedad_en_empresa', models.DateField(verbose_name='Antiguedad en la Empresa')),
                ('estudios_cursados', models.TextField(max_length=300, verbose_name='Estudios del Trabajador')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.BooleanField(verbose_name='Clickea para seleccionar turno "Tarde"')),
            ],
        ),
        migrations.AddField(
            model_name='grado',
            name='turno_asignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.Turno'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='prof_asignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.Profesor'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='seccion_asignada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.Seccion'),
        ),
    ]