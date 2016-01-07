from .models import Clinica
from .serializers import ClinicaSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

# class ClinicaList(APIView):
#     """
#     List all clinica, or create a new clinica.
#     """
#     def get(self, request, format=None):
#         clinicas = Clinica.objects.all()
#         serializer = ClinicaSerializer(clinicas, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ClinicaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClinicaList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
        queryset = Clinica.objects.all()
        serializer_class = ClinicaSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)


# class ClinicaDetail(APIView):
#         """
#         Retrieve, update or delete a clinica instance.
#         """
#         def get_object(self, pk):
#             try:
#                 return Clinica.objects.get(pk=pk)
#             except Clinica.DoesNotExist:
#                 raise Http404
#
#         def get(self, request, pk, format=None):
#             clinica = self.get_object(pk)
#             serializer = ClinicaSerializer(clinica)
#             return Response(serializer.data)
#
#         def put(self, request, pk, format=None):
#             clinica = self.get_object(pk)
#             serializer = ClinicaSerializer(clinica, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         def delete(self, request, pk, format=None):
#             clinica = self.get_object(pk)
#             clinica.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)


class ClinicaDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
        queryset = Clinica.objects.all()
        serializer_class = ClinicaSerializer

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
