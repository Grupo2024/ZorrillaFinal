# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0010_auto_20180628_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='fecha_nacimiento',
            field=models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='autorizado',
            name='fecha_nacimiento',
            field=models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='padre_madre',
            name='fecha_nacimiento',
            field=models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='fecha_nacimiento',
            field=models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='transportista',
            name='fecha_nacimiento',
            field=models.DateField(default='2000-10-10', verbose_name='Fecha de nacimiento'),
        ),
    ]