# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Especie, Raza


class EspecieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especie
        fields = ('id',
                  'nombre')


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = ('id',
                  'nombre',
                  'especie')


class RazaDetailSerializer(serializers.ModelSerializer):
    especie = EspecieSerializer(read_only=True)

    class Meta:
        model = Raza
        fields = ('id',
                  'nombre',
                  'especie')
