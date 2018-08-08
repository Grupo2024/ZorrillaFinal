# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-07 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0004_auto_20180807_1200'),
        ('matriculacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='grado_asignado',
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.CASCADE, to='institucion.Curso'),
            preserve_default=False,
        ),
    ]