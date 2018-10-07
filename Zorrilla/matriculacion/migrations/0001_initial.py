# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-07 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institucion', '0002_auto_20180923_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=40, verbose_name='Apellido')),
                ('dni', models.IntegerField(primary_key=True, serialize=False, verbose_name='Dni')),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=150, verbose_name='Lugar de Nacimiento')),
                ('fecha_nacimiento', models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento')),
                ('domicilio', models.CharField(blank=True, max_length=150, verbose_name='Domicilio')),
                ('email', models.EmailField(blank=True, max_length=70, verbose_name='Email')),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6, verbose_name='Sexo')),
                ('telefono_casa', models.IntegerField(verbose_name='Telefono de la Casa')),
                ('telefono_padre', models.IntegerField(null=True, verbose_name='Telefono del Padre')),
                ('telefono_madre', models.IntegerField(null=True, verbose_name='Telefono de la Madre')),
                ('telefono_familiar', models.IntegerField(null=True, verbose_name='Telefono de algun Familiar')),
                ('telefono_vecino', models.IntegerField(null=True, verbose_name='Telefono de algun Vecino')),
                ('enfermedad_relevante', models.CharField(max_length=40, null=True, verbose_name='Enfermedad relevante')),
                ('con_quien_vive', models.CharField(max_length=40, verbose_name='Con quien vive')),
                ('quien_lo_trae', models.CharField(max_length=40, verbose_name='Quien lo trae')),
                ('telefono_que_lo_trae', models.IntegerField(verbose_name='Telefono de quien lo trae')),
                ('numero_afiliado_obra_social', models.IntegerField(null=True, verbose_name='Numero de Afiliado')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='alumno_Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institucion.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Autorizado',
            fields=[
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=40, verbose_name='Apellido')),
                ('dni', models.IntegerField(primary_key=True, serialize=False, verbose_name='Dni')),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=150, verbose_name='Lugar de Nacimiento')),
                ('fecha_nacimiento', models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento')),
                ('domicilio', models.CharField(blank=True, max_length=150, verbose_name='Domicilio')),
                ('email', models.EmailField(blank=True, max_length=70, verbose_name='Email')),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6, verbose_name='Sexo')),
                ('telefono_autorizado', models.IntegerField(verbose_name='Telefono del autorizado')),
                ('relacion_con_alumno', models.TextField(max_length=300, verbose_name='Que relacion tiene con el alumno')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Alumno')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Matriculacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matriculacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Matriculacion')),
                ('matriculado', models.BooleanField(default=False, verbose_name='Esta matriculado o no')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Obra_Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obra_social_nombre', models.CharField(max_length=40, null=True, verbose_name='Nombre Obra Social')),
            ],
        ),
        migrations.CreateModel(
            name='Padre_madre',
            fields=[
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=40, verbose_name='Apellido')),
                ('dni', models.IntegerField(primary_key=True, serialize=False, verbose_name='Dni')),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=150, verbose_name='Lugar de Nacimiento')),
                ('fecha_nacimiento', models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento')),
                ('domicilio', models.CharField(blank=True, max_length=150, verbose_name='Domicilio')),
                ('email', models.EmailField(blank=True, max_length=70, verbose_name='Email')),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6, verbose_name='Sexo')),
                ('profesion', models.CharField(max_length=40, verbose_name='Profesion del Padre/Madre')),
                ('telefono_trabajo', models.IntegerField(verbose_name='Telefono del Trabajo del Padre/Madre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=40, verbose_name='Apellido')),
                ('dni', models.IntegerField(primary_key=True, serialize=False, verbose_name='Dni')),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=150, verbose_name='Lugar de Nacimiento')),
                ('fecha_nacimiento', models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento')),
                ('domicilio', models.CharField(blank=True, max_length=150, verbose_name='Domicilio')),
                ('email', models.EmailField(blank=True, max_length=70, verbose_name='Email')),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=6, verbose_name='Sexo')),
                ('nombre_transporte', models.CharField(max_length=40, verbose_name='Nombre del Transporte')),
                ('telefono_transportista', models.IntegerField(verbose_name='Telefono del Transportista')),
                ('detalles_transportista', models.TextField(max_length=300, verbose_name='Detalles del Transportista')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='usa_Obra_Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obra_social_numero', models.IntegerField(verbose_name='Num Obra Social')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Alumno')),
                ('obra_social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Obra_Social')),
            ],
        ),
        migrations.CreateModel(
            name='usa_Transporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Alumno')),
                ('transportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Transportista')),
            ],
        ),
        migrations.AddField(
            model_name='familia',
            name='padre_madre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Padre_madre'),
        ),
    ]
