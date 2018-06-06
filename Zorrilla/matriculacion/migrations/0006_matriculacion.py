# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-29 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0005_auto_20180522_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matriculacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matriculacion', models.DateTimeField(blank=True, verbose_name='Fecha Matriculacion')),
                ('matriculado', models.BooleanField(default=False, verbose_name='Esta matriculado o no')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriculacion.Alumno')),
            ],
        ),
    ]