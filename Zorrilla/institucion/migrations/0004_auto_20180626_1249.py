# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0003_auto_20180626_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clave_docente',
            name='dni_docente',
            field=models.IntegerField(),
        ),
    ]
