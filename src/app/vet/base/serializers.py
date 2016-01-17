# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Clinica
from app.recursos.localidades.serializers import ComunaDetailSerializer


class ClinicaDetailSerializer(serializers.ModelSerializer):
    comuna = ComunaDetailSerializer()

    class Meta:
        model = Clinica
        fields = ('id',
                  'nombre',
                  'rut',
                  'representante',
                  'direccion',
                  'comuna',
                  'correo_electronico',
                  'telefono')
