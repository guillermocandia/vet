# -*- coding: utf-8 -*-
from django.db import models


class Region(models.Model):
    """
    Regiones
    """
    nombre = models.CharField(
        'Nombre',
        max_length=64,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'


class Provincia(models.Model):
    """
    Provincias
    """
    nombre = models.CharField(
        'Nombre',
        max_length=64,
        blank=False,
        null=False
    )

    region = models.ForeignKey(Region, related_name='provincias')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'


class Comuna(models.Model):
    """
    Comunas
    """
    nombre = models.CharField(
        'Nombre',
        max_length=64,
        blank=False,
        null=False
    )

    provincia = models.ForeignKey(Provincia, related_name='comunas')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
