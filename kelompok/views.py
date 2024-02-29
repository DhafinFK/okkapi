from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import KelompokSerializer, MentoringSerializer
from .models import *

# Create your views here.


class KelompokList(APIView):
    """
    List semua kelompok dan create kelompok baru
    """
    def get(self, requesst, format=None):
        kelompok = Kelompok.objects.all()
        serializer = KelompokSerializer(kelompok, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = KelompokSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KelompokDetail(APIView):
    """
    Detail, buat, update kelompok tertentu
    """
    def get_fakultas(self, nomor):
        try:
            kelompok = Kelompok.objects.get(nomor=nomor)
            return kelompok
        except Kelompok.DoesNotExist:
            raise Http404

    def get(self, request, nomor, format=None):
        kelompok = self.get_fakultas(nomor)
        serializer = KelompokSerializer(kelompok)
        return Response(serializer.data)
    
    def delete(self, request, nomor, format=None):
        kelompok = self.get_fakultas(nomor)
        kelompok.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, nomor, format=None):
        kelompok = self.get_fakultas(nomor)
        serializer = KelompokSerializer(kelompok, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, nomor, format=None):
        kelompok = self.get_fakultas(nomor)
        serializer = KelompokSerializer(kelompok, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class MentoringList(APIView):
    def get(self, request, nomor, format=None):
        sessions = MentoringSession.objects.filter(kelompok__nomor=nomor)
        serializer = MentoringSerializer(sessions, many=True)
        return Response(serializer.data)
    
    def post(self, request, nomor, format=None):
        serializer = MentoringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MentoringDetail(APIView):
    """
    Detail, buat, update kelompok tertentu
    """
    def get_mentoring_session(self, nomor, id):
        try:
            session = MentoringSession.objects.get(id=id, kelompok__nomor=nomor)
            return session
        except Kelompok.DoesNotExist:
            raise Http404

    def get(self, request, nomor, id, format=None):
        session = self.get_mentoring_session(nomor)
        serializer = MentoringSerializer(session)
        return Response(serializer.data)
    
    def delete(self, request, nomor, id, format=None):
        session = self.get_mentoring_session(nomor, id)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, nomor, id, format=None):
        session = self.get_mentoring_session(nomor, id)
        serializer = MentoringSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, nomor, id, format=None):
        session = self.get_mentoring_session(nomor, id)
        serializer = MentoringSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    