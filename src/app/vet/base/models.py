# -*- coding: utf-8 -*-
from django.db import models

from app.recursos.localidades.models import Comuna


class Clinica(models.Model):
    """
    Clínica
    """
    nombre = models.CharField(
        'Clínica',
        max_length=64,
        blank=False,
        null=False
    )
    rut = models.CharField(
        'Rut',
        max_length=32,
        blank=False,
        null=False
    )
    representante = models.CharField(
        'Representante',
        max_length=128,
        blank=False,
        null=False
    )
    direccion = models.CharField(
        'Dirección',
        max_length=512,
        blank=False,
        null=False
    )
    comuna = models.ForeignKey(
        Comuna,
        blank=False,
        null=False,
        related_name='comuna'
    )
    correo_electronico = models.EmailField(
        'Correo electrónico',
        max_length=64,
        blank=False,
        null=False
    )
    telefono = models.CharField(
        'Teléfono',
        max_length=32,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = 'Datos clínica'
        verbose_name_plural = 'Datos clínica'

    def __str__(self):
        return self.nombre
