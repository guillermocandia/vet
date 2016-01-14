# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Region, Provincia, Comuna


class RegionSerializer(serializers.ModelSerializer):
        class Meta:
            model = Region
            fields = ('id',
                      'nombre')


class ProvinciaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Provincia
            fields = ('id',
                      'nombre',
                      'region')


class ComunaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comuna
            fields = ('id',
                      'nombre',
                      'provincia')
