from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import Http404
from .models import *
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


class MentorList(APIView):

    permission_classes = [IsSuperUser]

    def get(self, request, format=None):
        semua_mentor = Mentor.objects.all()
        serializer = MentorSerializer(semua_mentor, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MentorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class MenteeDetail(APIView):

    permission_classes = [IsSuperUser]
    
    def get_mentee(self, id):
        try:
            mentee = Mentee.objects.get(id=id)
            return mentee
        except Mentee.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        mentee = self.get_mentee(id)
        serializers = MenteeSerializer(mentee)
        return Response(serializers.data)
    
    def delete(self, request, id, format=None):
        mentee = self.get_mentee(id)
        mentee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        mentee = self.get_mentee(id)
        serializer = MenteeSerializer(mentee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        mentee = self.get_mentee(id)
        serializer = MenteeSerializer(mentee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MenteeList(APIView):

    permission_classes = [IsSuperUser]

    def get(self, request, format=None):
        semua_mentee = Mentee.objects.all()
        serializer = MenteeSerializer(semua_mentee, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MenteeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class MentorDetail(APIView):

    permission_classes = [IsSuperUser]
    
    def get_mentor(self, id):
        try:
            mentor = Mentor.objects.get(id=id)
            return mentor
        except Mentor.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        mentor = self.get_mentor(id)
        serializers = MentorSerializer(mentor)
        return Response(serializers.data)
    
    def delete(self, request, id, format=None):
        mentor = self.get_mentor(id)
        mentor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        mentor = self.get_mentor(id)
        serializer = MentorSerializer(mentor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        mentor = self.get_mentor(id)
        serializer = MentorSerializer(mentor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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
    
