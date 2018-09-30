# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0002_auto_20180923_1731'),
        ('matriculacion', '0011_auto_20180923_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='institucion.Curso'),
            preserve_default=False,
        ),
    ]