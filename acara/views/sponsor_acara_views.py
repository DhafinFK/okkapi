from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from acara.serializers import SponsorAcaraSerializer
from acara.models import SponsorAcara
from custom_auth.permissions import IsPanitiaPermission


class SponsorAcaraList(APIView):

    permission_classes = [IsPanitiaPermission]

    def get(self, request):
        sponsor_acara = SponsorAcara.objects.all()
        serializer = SponsorAcaraSerializer(sponsor_acara, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SponsorAcaraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class SponsorAcaraDetail(APIView):

    permission_classes = [IsPanitiaPermission]

    def get_sponsor_acara(self, id):
        try:
            sponsor = SponsorAcara.objects.get(id=id)
            return sponsor
        except SponsorAcara.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        sponsor_acara = self.get_sponsor_acara(id)
        serializer = SponsorAcaraSerializer(sponsor_acara)
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        sponsor_acara = self.get_sponsor_acara(id)
        sponsor_acara.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        sponsor_acara = self.get_sponsor_acara(id)
        serializer = SponsorAcaraSerializer(sponsor_acara, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        sponsor_acara = self.get_sponsor_acara(id)
        serializer = SponsorAcaraSerializer(sponsor_acara, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    