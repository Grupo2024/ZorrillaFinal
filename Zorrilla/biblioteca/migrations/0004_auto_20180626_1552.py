# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-26 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_auto_20180618_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='cantidad_paginas',
            field=models.IntegerField(null=True),
        ),
    ]
