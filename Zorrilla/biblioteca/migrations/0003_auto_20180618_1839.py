# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20180618_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='document',
            field=models.ForeignKey(default=32, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Document'),
            preserve_default=False,
        ),
    ]
