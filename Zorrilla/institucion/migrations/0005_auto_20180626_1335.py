# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0004_auto_20180626_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clave_docente',
            name='clave_logIn',
            field=models.CharField(max_length=10),
        ),
    ]
