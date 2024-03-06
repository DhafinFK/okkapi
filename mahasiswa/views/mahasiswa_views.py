from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mahasiswa.serializers import MahasiswaSerializer
from django.http import Http404
from mahasiswa.models import Mahasiswa
from custom_auth.permissions import IsSuperUser

# Create your views here.

class MahasiswaList(APIView):
    """
    List semua mahasisswa dan data terkait
    """
    permission_classes = [IsSuperUser]

    def get(self, request, format=None):
        mahasiswa = Mahasiswa.objects.all()
        serializer = MahasiswaSerializer(mahasiswa, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MahasiswaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MahasiswaDetail(APIView):

    permission_classes = [IsSuperUser]

    def get_mahasiswa(self, id):
        try:
            mahasiswa = Mahasiswa.objects.get(id=id)
            return mahasiswa
        except Mahasiswa.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        mahasiswa = self.get_mahasiswa(id)
        serializer = MahasiswaSerializer(mahasiswa)
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        mahasiswa = self.get_mahasiswa(id)
        mahasiswa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        mahasiswa = self.get_mahasiswa(id)
        serializer = MahasiswaSerializer(mahasiswa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id, format=None):
        mahasiswa = self.get_mahasiswa(id)
        serializer = MahasiswaSerializer(mahasiswa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)