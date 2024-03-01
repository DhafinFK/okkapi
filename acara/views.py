from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from .models import *

# Create your views here.

class AcaraList(APIView):
    """
    List semua acara dan create Acara
    """
    def get(self, request, format=None):
        acara_acara = Acara.objects.all()
        serializer = AcaraSerializer(acara_acara, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AcaraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class AcaraDetail(APIView):
    """
    Detail, buat, update acara tertentu
    """
    def get_acara(self, id):
        try:
            acara = Acara.objects.get(id=id)
            return acara
        except Acara.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Acara = self.get_acara(id)
        serializer = AcaraSerializer(Acara)
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        acara = self.get_acara(id)
        acara.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        acara = self.get_acara(id)
        serializer = AcaraSerializer(acara, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # TODO: fix or remove partial on patch. It broke...
    def patch(self, request, id, format=None):
        acara = self.get_acara(id)
        serializer = AcaraSerializer(acara, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class PembicaraList(APIView):
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
    def get_pembicara(self, id):
        try:
            pembicara = Pembicara.objects.get(id=id)
            return pembicara
        except Pembicara.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Pembicara = self.get_pembicara(id)
        serializer = PembicaraSerializer(Pembicara)
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
        
    