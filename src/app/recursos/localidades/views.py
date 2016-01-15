# -*- coding: utf-8 -*-
from rest_framework import generics

from .models import Region, Provincia, Comuna
from .serializers import RegionSerializer
from .serializers import ProvinciaSerializer
from .serializers import ComunaSerializer
from .serializers import ComunaDetailSerializer
from .serializers import ProvinciaDetailSerializer


class RegionesList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ProvinciasList(generics.ListAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class ComunasList(generics.ListAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class RegionDetail(generics.RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ProvinciaDetail(generics.RetrieveAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaDetailSerializer


class ComunaDetail(generics.RetrieveAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaDetailSerializer


class RegionProvinciasList(generics.ListAPIView):
    serializer_class = ProvinciaSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Provincia.objects.filter(region_id=pk)


class RegionComunasList(generics.ListAPIView):
    serializer_class = ComunaSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comuna.objects.filter(provincia__region_id=pk)


class ProvinciaComunasList(generics.ListAPIView):
    serializer_class = ComunaSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comuna.objects.filter(provincia_id=pk)
