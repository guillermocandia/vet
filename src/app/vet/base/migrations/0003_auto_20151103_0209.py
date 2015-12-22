# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.vet.base.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151103_0003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clinica',
            options={'verbose_name': 'Datos clínica', 'verbose_name_plural': 'Datos clínica'},
        ),
        migrations.RenameField(
            model_name='clinica',
            old_name='correo_electrónico',
            new_name='correo_electronico',
        ),
        migrations.AlterField(
            model_name='clinica',
            name='logo',
            field=models.ImageField(verbose_name='Logo', null=True, upload_to=app.vet.base.models.upload_image_to),
        ),
    ]
