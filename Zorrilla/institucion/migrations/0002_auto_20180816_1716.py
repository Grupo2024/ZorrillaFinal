# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-16 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='sexo_t',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=15, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='sexo_t',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=15, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='sexo_t',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=15, verbose_name='Sexo'),
        ),
    ]
