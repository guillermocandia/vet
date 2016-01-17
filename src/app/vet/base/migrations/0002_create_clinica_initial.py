# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def create_clinica(apps, schema_editor):
    # Crea la clínica inicial con datos predeterminados
    # Para modificar los datos se debe usar django-admin
    Clinica = apps.get_model('base', 'Clinica')
    Comuna = apps.get_model('localidades', 'Comuna')

    comuna = Comuna.objects.get(nombre='Valparaíso')

    clinica = Clinica()
    clinica.pk = 1
    clinica. nombre = 'Clínica Veterinaria'
    clinica.rut = '13245678-5'
    clinica.representante = 'Nombre Representante'
    clinica.direccion = 'Dirección'
    clinica.comuna = comuna
    clinica.correo_electronico = 'correo@correo.com'
    clinica.telefono = '+56912345678'
    clinica.save()


def delete_clinica(apps, schema_editor):
    # Borra la clínica inicial
    Clinica = apps.get_model('base', 'Clinica')
    clinica = Clinica.objects.get(pk=1)
    clinica.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('localidades', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_clinica, delete_clinica),
    ]
