# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='document_id',
        ),
        migrations.AddField(
            model_name='document',
            name='id',
            field=models.AutoField(auto_created=True, default=3, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
