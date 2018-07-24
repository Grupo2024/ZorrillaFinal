# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=60)),
                ('genero', models.CharField(choices=[('Drama', 'Drama'), ('Romance', 'Romance'), ('Accion', 'Accion'), ('Ciencia Ficcion', 'Ciencia Ficcion'), ('Terror', 'Terror'), ('Aventura', 'Aventura'), ('Policial', 'Policial'), ('Politica', 'Politica'), ('Fantasia', 'Fantasia'), ('Otros', 'Otros')], max_length=15, verbose_name='Modificacion')),
                ('autor', models.CharField(max_length=60)),
                ('habilitado', models.BooleanField(default=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modificacion', models.CharField(choices=[('Habilitar', 'Habilitar'), ('Deshabilitar', 'Deshabilitar'), ('Eliminar', 'Eliminar'), ('Crear', 'Crear'), ('Editar', 'Editar')], max_length=12, verbose_name='Modificacion')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.Document')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
