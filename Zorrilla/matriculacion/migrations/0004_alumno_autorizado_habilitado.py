# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0003_auto_20181024_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno_autorizado',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]