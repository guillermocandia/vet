# -*- coding: utf-8 -*-
from rest_framework import generics

from .models import Especie, Raza
from .serializers import EspecieSerializer
from .serializers import RazaSerializer
from .serializers import RazaDetailSerializer


class EspecieList(generics.ListCreateAPIView):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer


class EspecieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer


class RazaList(generics.ListCreateAPIView):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer


class RazaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Raza.objects.all()
    serializer_class = RazaDetailSerializer


class EspecieRazaList(generics.ListAPIView):
    serializer_class = RazaSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Raza.objects.filter(especie_id=pk)
