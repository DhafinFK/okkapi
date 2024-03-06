from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mahasiswa.serializers import MenteeSerializer
from mahasiswa.models import Mentee
from django.http import Http404
from custom_auth.permissions import IsSuperUser
    

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