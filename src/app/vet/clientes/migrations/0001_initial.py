# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(unique=True, verbose_name='Nombre', max_length=64)),
            ],
            options={
                'verbose_name': 'Especie',
                'verbose_name_plural': 'Especies',
            },
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(verbose_name='Nombre', max_length=64)),
                ('especie', models.ForeignKey(related_name='razas', to='clientes.Especie', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'verbose_name': 'Raza',
                'verbose_name_plural': 'Razas',
            },
        ),
        migrations.AlterUniqueTogether(
            name='raza',
            unique_together=set([('nombre', 'especie')]),
        ),
    ]
