from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Clinica
from .serializers import ClinicaSerializer


@api_view(['GET', 'POST'])
def clinica_list(request, format=None):
    """
    List all code snippets, or create a new Clinica.
    """
    if request.method == 'GET':
        clinicas = Clinica.objects.all()
        serializer = ClinicaSerializer(clinicas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClinicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def clinica_detail(request, pk, format=None):
    """
    Retrieve, update or delete a Clinica.
    """
    try:
        clinica = Clinica.objects.get(pk=pk)
    except Clinica.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClinicaSerializer(clinica)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClinicaSerializer(clinica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        clinica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
