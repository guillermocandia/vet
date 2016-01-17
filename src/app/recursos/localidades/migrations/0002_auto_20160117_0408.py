# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='provincia',
            field=models.ForeignKey(to='localidades.Provincia', related_name='comunas'),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='region',
            field=models.ForeignKey(to='localidades.Region', related_name='provincias'),
        ),
    ]
