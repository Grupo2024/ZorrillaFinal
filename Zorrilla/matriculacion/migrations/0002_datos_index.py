# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='datos_Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.IntegerField()),
                ('telefono2', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
            ],
        ),
    ]
