# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Clinica


class ClinicaSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Clinica
            fields = ('id',
                      'url',
                      'nombre',
                      'direccion',
                      'ciudad',
                      'correo_electronico',
                      'telefono_fijo',
                      'telefono_movil')

# class ClinicaSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     nombre = serializers.CharField(
#         required=True,
#         allow_blank=False,
#         max_length=128
#     )
#
# #     logo = models.ImageField(
# #         'Logo',
# #         upload_to=upload_image_to,
# #         null=True
# #     )
#
#     direccion = serializers.CharField(
#         required=True,
#         allow_blank=False,
#         max_length=128
#     )
#
#     ciudad = serializers.CharField(
#         required=False,
#         allow_blank=True,
#         max_length=128
#     )
#
#     correo_electronico = serializers.CharField(
#         required=False,
#         allow_blank=False,
#         max_length=128
#     )
#
#     telefono_fijo = serializers.CharField(
#         required=False,
#         allow_blank=True,
#         max_length=128
#     )
#
#     telefono_movil = serializers.CharField(
#         required=False,
#         allow_blank=True,
#         max_length=128
#     )
#
#     def create(self, validated_data):
#         """
#         Crea y retorna una instancia de Clinica con los datos validados.
#         """
#         return Clinica.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Actualiza y retorna una instancia de Clinica con los datos validados.
#         """
#         instance.nombre = validated_data.get(
#             'nombre', instance.nombre)
#         instance.direccion = validated_data.get(
#             'direccion', instance.direccion)
#         instance.ciudad = validated_data.get(
#             'ciudad', instance.ciudad)
#         instance.correo_electronico = validated_data.get(
#             'correo_electronico', instance.correo_electronico)
#         instance.telefono_fijo = validated_data.get(
#             'telefono_fijo', instance.telefono_fijo)
#         instance.telefono_movil = validated_data.get(
#             'telefono_movil', instance.telefono_movil)
#         instance.save()
#         return instance
