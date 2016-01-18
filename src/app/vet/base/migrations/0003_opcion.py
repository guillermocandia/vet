# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_create_clinica_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=64, verbose_name='Nombre')),
                ('valor', models.CharField(max_length=64, verbose_name='Valor')),
                ('descripcion', models.CharField(max_length=256, verbose_name='Descripción', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Opción',
                'verbose_name_plural': 'Opciones',
            },
        ),
    ]
