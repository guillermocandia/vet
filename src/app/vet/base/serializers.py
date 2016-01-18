# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Clinica, Opcion
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


class OpcionSerializer(serializers.ModelSerializer):
    nombre = serializers.ReadOnlyField()
    descripcion = serializers.ReadOnlyField()

    class Meta:
        model = Opcion
        fields = ('id',
                  'nombre',
                  'valor',
                  'descripcion')
