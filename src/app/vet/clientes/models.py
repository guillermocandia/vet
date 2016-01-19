# -*- coding: utf-8 -*-
from django.db import models


class Especie(models.Model):
    """
    Especie
    """
    nombre = models.CharField(
        'Nombre',
        max_length=64,
        blank=False,
        null=False,
        unique=True
    )

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'

    def __str__(self):
        return self.nombre


class Raza(models.Model):
    """
    Raza
    """
    nombre = models.CharField(
        'Nombre',
        max_length=64,
        blank=False,
        null=False
    )
    especie = models.ForeignKey(
        Especie,
        blank=False,
        null=False,
        related_name='razas',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'
        unique_together = ('nombre', 'especie')

    def __str__(self):
        return self.nombre
