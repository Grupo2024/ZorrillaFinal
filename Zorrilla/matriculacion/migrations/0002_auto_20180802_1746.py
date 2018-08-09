# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-02 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='seccion_asignada',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='institucion.Seccion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='sexo',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=15, verbose_name='Modificacion'),
        ),
        migrations.AlterField(
            model_name='autorizado',
            name='sexo',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=15, verbose_name='Modificacion'),
        ),
        migrations.AlterField(
            model_name='padre_madre',
            name='sexo',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=15, verbose_name='Modificacion'),
        ),
        migrations.AlterField(
            model_name='transportista',
            name='sexo',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=15, verbose_name='Modificacion'),
        ),
    ]
