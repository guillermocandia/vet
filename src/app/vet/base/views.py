from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Clinica
from .serializers import ClinicaSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def clinica_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        clinicas = Clinica.objects.all()
        serializer = ClinicaSerializer(clinicas, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClinicaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def clinica_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        clinica = Clinica.objects.get(pk=pk)
    except Clinica.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClinicaSerializer(clinica)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClinicaSerializer(clinica, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        clinica.delete()
        return HttpResponse(status=204)
