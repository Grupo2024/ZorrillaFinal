# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0003_auto_20181007_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clave_docente',
            name='dni_docente',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='clave_docente',
            name='email_docente',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
