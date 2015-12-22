# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinica',
            name='ciudad',
            field=models.CharField(verbose_name='Ciudad', blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='correo_electrónico',
            field=models.EmailField(verbose_name='Correo electrónico', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='logo',
            field=models.ImageField(upload_to='', verbose_name='Logo', null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='telefono_fijo',
            field=models.CharField(verbose_name='Teléfono fijo', blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='clinica',
            name='telefono_movil',
            field=models.CharField(verbose_name='Teléfono móvil', blank=True, max_length=128, null=True),
        ),
    ]
