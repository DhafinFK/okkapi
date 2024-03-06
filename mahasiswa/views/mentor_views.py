from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mahasiswa.serializers import MentorSerializer
from mahasiswa.models import Mentor
from django.http import Http404
from custom_auth.permissions import IsSuperUser


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