# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clinica',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128, verbose_name='Clínica')),
                ('direccion', models.CharField(blank=True, max_length=128, verbose_name='Dirección', null=True)),
            ],
        ),
    ]
