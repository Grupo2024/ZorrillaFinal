# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-28 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0003_seccion_prof_asignado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='fecha_nacimiento_t',
            field=models.DateField(blank=True, verbose_name='Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='fecha_nacimiento_t',
            field=models.DateField(blank=True, verbose_name='Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='fecha_nacimiento_t',
            field=models.DateField(blank=True, verbose_name='Fecha Nacimiento'),
        ),
    ]
