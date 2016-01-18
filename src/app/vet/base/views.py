# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import generics

from .models import Clinica, Opcion
from .serializers import ClinicaDetailSerializer, OpcionSerializer


class ClinicaDetail(APIView):
    """
    Retorna la primera y única Clínica
    """
    def get_object(self):
        try:
            return Clinica.objects.first()
        except Clinica.DoesNotExist:
            raise Http404

    def get(self, request):
        clinica = self.get_object()
        serializer = ClinicaDetailSerializer(clinica)
        return Response(serializer.data)


class OpcionList(generics.ListAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer


class OpcionDetail(generics.RetrieveUpdateAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer


class OpcionNombreDetail(generics.RetrieveAPIView):
    lookup_field = 'nombre'
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
