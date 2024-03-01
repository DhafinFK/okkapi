from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BidangKepanitiaanSerializer, RapatSerializer
from .models import BidangKepanitiaan, Rapat
from common.permissions import IsPanitiaPermission

# Create your views here.

class BidangList(APIView):
    permission_classes = [IsPanitiaPermission]

    def get(self, requesst, format=None):
        bidang = BidangKepanitiaan.objects.all()
        serializer = BidangKepanitiaanSerializer(bidang, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BidangKepanitiaanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BidangDetail(APIView):
    """
    Detail, buat, update bidang tertentu
    """
    def get_bidang(self, id):
        try:
            bidang = BidangKepanitiaan.objects.get(id=id)
            return bidang
        except BidangKepanitiaan.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        bidang = self.get_bidang(id)
        serializer = BidangKepanitiaanSerializer(bidang)
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        bidang = self.get_bidang(id)
        bidang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        bidang = self.get_bidang(id)
        serializer = BidangKepanitiaanSerializer(bidang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        bidang = self.get_bidang(id)
        serializer = BidangKepanitiaanSerializer(bidang, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class RapatList(APIView):
    def get(self, request, bidang_id, format=None):
        sessions = Rapat.objects.filter(bidang=bidang_id)
        serializer = RapatSerializer(sessions, many=True)
        return Response(serializer.data)
    
    def post(self, request, bidang_id, format=None):
        serializer = RapatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RapatDetail(APIView):
    """
    Detail, buat, update kelompok tertentu
    """
    def get_mentoring_session(self, bidang_id, id):
        try:
            session = Rapat.objects.get(id=id, bidang_id=bidang_id)
            return session
        except BidangKepanitiaan.DoesNotExist:
            raise Http404

    def get(self, request, bidang_id, id, format=None):
        session = self.get_mentoring_session(bidang_id, id)
        serializer = RapatSerializer(session)
        return Response(serializer.data)
    
    def delete(self, request, bidang_id, id, format=None):
        session = self.get_mentoring_session(bidang_id, id)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, bidang_id, id, format=None):
        session = self.get_mentoring_session(bidang_id, id)
        serializer = RapatSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, bidang_id, id, format=None):
        session = self.get_mentoring_session(bidang_id, id)
        serializer = RapatSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    