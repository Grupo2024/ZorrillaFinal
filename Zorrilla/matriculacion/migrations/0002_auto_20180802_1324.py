# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-02 13:24
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
            field=models.ForeignKey(blank=True, default=3123, on_delete=django.db.models.deletion.CASCADE, to='institucion.Seccion'),
            preserve_default=False,
        ),
    ]