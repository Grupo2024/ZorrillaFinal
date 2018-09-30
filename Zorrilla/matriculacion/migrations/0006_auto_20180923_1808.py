# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0005_auto_20180923_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='con_quien_vive',
            field=models.CharField(max_length=40, null=True, verbose_name='Con quien vive'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='quien_lo_trae',
            field=models.CharField(max_length=40, null=True, verbose_name='Quien lo trae'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono_que_lo_trae',
            field=models.IntegerField(null=True, verbose_name='Telefono de quien lo trae'),
        ),
    ]