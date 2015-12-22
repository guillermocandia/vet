# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


def upload_image_to(instance, filename):
    from django.utils.timezone import now
    return '%s/logo/%s_%s' % (
        settings.CLIENTE_ID,
        now().strftime("%Y%m%d%H%M%S"),
        filename.lower(),
    )


class Clinica(models.Model):
    nombre = models.CharField(
        'Clínica',
        max_length=128,
        blank=False,
        null=False
    )
#     logo = models.ImageField(
#         'Logo',
#         upload_to=upload_image_to,
#         null=True
#     )
    direccion = models.CharField(
        'Dirección',
        max_length=128,
        blank=True,
        null=True
    )
    ciudad = models.CharField(
        'Ciudad',
        max_length=128,
        blank=True,
        null=True
    )
    correo_electronico = models.EmailField(
        'Correo electrónico',
        max_length=128,
        blank=False,
        null=True
    )
    telefono_fijo = models.CharField(
        'Teléfono fijo',
        max_length=128,
        blank=True,
        null=True
    )
    telefono_movil = models.CharField(
        'Teléfono móvil',
        max_length=128,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Datos clínica'
        verbose_name_plural = 'Datos clínica'

        permissions = (
            ('editar_clinica', 'Puede editar Clínica'),
        )

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
