# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0002_remove_familia_secretaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usa_obra_social',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usa_transporte',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
