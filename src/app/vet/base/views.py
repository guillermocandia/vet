# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

from .models import Clinica
from .serializers import ClinicaDetailSerializer


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
