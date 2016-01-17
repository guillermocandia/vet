# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localidades', '0002_auto_20160117_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(verbose_name='Clínica', max_length=64)),
                ('rut', models.CharField(verbose_name='Rut', max_length=32)),
                ('representante', models.CharField(verbose_name='Representante', max_length=128)),
                ('direccion', models.CharField(verbose_name='Dirección', max_length=512)),
                ('correo_electronico', models.EmailField(verbose_name='Correo electrónico', max_length=64)),
                ('telefono', models.CharField(verbose_name='Teléfono', max_length=32)),
                ('comuna', models.ForeignKey(to='localidades.Comuna', related_name='comuna')),
            ],
            options={
                'verbose_name_plural': 'Datos clínica',
                'verbose_name': 'Datos clínica',
            },
        ),
    ]
