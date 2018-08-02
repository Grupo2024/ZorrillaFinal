# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institucion', '0001_initial'),
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
                ('sexo', models.BooleanField(verbose_name='Sexo')),
                ('telefono_casa', models.IntegerField(verbose_name='Telefono de la Casa')),
                ('telefono_padre', models.IntegerField(null=True, verbose_name='Telefono del Padre')),
                ('telefono_madre', models.IntegerField(null=True, verbose_name='Telefono de la Madre')),
                ('telefono_familiar', models.IntegerField(null=True, verbose_name='Telefono de algun Familiar')),
                ('telefono_vecino', models.IntegerField(null=True, verbose_name='Telefono de algun Vecino')),
                ('enfermedad_relevante', models.CharField(max_length=40, null=True, verbose_name='Enfermedad relevante')),
                ('con_quien_vive', models.CharField(max_length=40, verbose_name='Con quien vive')),
                ('quien_lo_trae', models.CharField(max_length=40, verbose_name='Quien lo trae')),
                ('telefono_que_lo_trae', models.IntegerField(verbose_name='Telefono de quien lo trae')),
                ('utiliza_transporte', models.BooleanField(verbose_name='Viene o no en transporte')),
                ('tiene_obra_social', models.BooleanField(verbose_name='Tiene obra o no')),
                ('obra_social_nombre', models.CharField(max_length=40, null=True, verbose_name='Nombre Obra Social')),
                ('obra_social_numero', models.IntegerField(verbose_name='Num Obra Social')),
                ('matriculado', models.BooleanField(verbose_name='Esta matriculado o no')),
            ],
            options={
                'abstract': False,
            },
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
                ('sexo', models.BooleanField(verbose_name='Sexo')),
                ('autorizacion', models.BooleanField(verbose_name='Esta autorizado o no')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Matriculacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matriculacion', models.DateTimeField(blank=True, verbose_name='Fecha Matriculacion')),
                ('matriculado', models.BooleanField(default=False, verbose_name='Esta matriculado o no')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Alumno')),
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
                ('sexo', models.BooleanField(verbose_name='Sexo')),
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
                ('sexo', models.BooleanField(verbose_name='Sexo')),
                ('nombre_transporte', models.CharField(max_length=40, verbose_name='Nombre del Transporte')),
                ('telefono_transportista', models.IntegerField(verbose_name='Telefono del Transportista')),
                ('detalles_transportista', models.TextField(max_length=300, verbose_name='Detalles del Transportista')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='autorizados',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Autorizado'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='padres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Padre_madre'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='seccion_asignada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institucion.Seccion'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='transporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Transportista'),
        ),
    ]