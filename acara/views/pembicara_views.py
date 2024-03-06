from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from acara.serializers import PembicaraSerializer
from acara.models import Pembicara
from custom_auth.permissions import IsPanitiaPermission

class PembicaraList(APIView):

    permission_classes = [IsPanitiaPermission]

    def get(self, request):
        pembicara = Pembicara.objects.all()
        serializer = PembicaraSerializer(pembicara, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PembicaraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class PembicaraDetail(APIView):

    permission_classes = [IsPanitiaPermission]

    def get_pembicara(self, id):
        try:
            pembicara = Pembicara.objects.get(id=id)
            return pembicara
        except Pembicara.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        pembicara = self.get_pembicara(id)
        serializer = PembicaraSerializer(pembicara)
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        pembicara = self.get_pembicara(id)
        pembicara.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        pembicara = self.get_pembicara(id)
        serializer = PembicaraSerializer(pembicara, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        pembicara = self.get_pembicara(id)
        serializer = PembicaraSerializer(pembicara, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        