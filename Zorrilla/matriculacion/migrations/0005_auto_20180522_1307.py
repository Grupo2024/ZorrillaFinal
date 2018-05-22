# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-22 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0004_auto_20180515_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='matriculado',
            field=models.BooleanField(default=False, verbose_name='Esta matriculado o no'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='autorizados',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Autorizado'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='padres',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Padre_madre'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='transporte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Transportista'),
        ),
    ]
