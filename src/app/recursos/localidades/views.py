from rest_framework import generics


from .models import Region, Provincia, Comuna
from .serializers import RegionSerializer
from .serializers import ProvinciaSerializer
from .serializers import ComunaSerializer


class RegionesList(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ProvinciasList(generics.ListAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class ComunasList(generics.ListAPIView):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer
