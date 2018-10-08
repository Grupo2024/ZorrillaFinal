# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0004_auto_20181008_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='email',
            field=models.EmailField(blank=True, max_length=70, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='autorizado',
            name='email',
            field=models.EmailField(blank=True, max_length=70, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='padre_madre',
            name='email',
            field=models.EmailField(blank=True, max_length=70, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='transportista',
            name='email',
            field=models.EmailField(blank=True, max_length=70, verbose_name='Email'),
        ),
    ]
