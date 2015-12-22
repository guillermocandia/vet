# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151103_0209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clinica',
            options={'verbose_name': 'Datos clínica', 'permissions': (('editar_clinica', 'Puede editar Clínica'),), 'verbose_name_plural': 'Datos clínica'},
        ),
    ]
