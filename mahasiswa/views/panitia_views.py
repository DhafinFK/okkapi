from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mahasiswa.serializers import PanitiaSerializer
from mahasiswa.models import Panitia
from django.http import Http404
from custom_auth.permissions import IsSuperUser
    

class PanitiaList(APIView):

    permission_classes = [IsSuperUser]

    def get(self, request, format=None):
        semua_panitia = Panitia.objects.all()
        serializer = PanitiaSerializer(semua_panitia, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PanitiaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PanitiaDetail(APIView):

    permission_classes = [IsSuperUser]

    def get_panitia(self, id):
        try:
            panitia = Panitia.objects.get(id=id)
            return panitia
        except Panitia.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        panitia = self.get_panitia(id)
        serializer = PanitiaSerializer(panitia)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        panitia = self.get_panitia(id)
        panitia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        panitia = self.get_panitia(id)
        serializer = PanitiaSerializer(panitia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        panitia = self.get_panitia(id)
        serializer = PanitiaSerializer(panitia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)