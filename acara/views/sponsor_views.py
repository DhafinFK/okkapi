from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from acara.serializers import SponsorSerializer
from acara.models import Sponsor
from custom_auth.permissions import IsPanitiaPermission

class SponsorList(APIView):

    permission_classes = [IsPanitiaPermission]

    def get(self, request):
        sponsor = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsor, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class SponsorDetail(APIView):
    
    permission_classes = [IsPanitiaPermission]

    def get_sponsor(self, id):
        try:
            sponsor = Sponsor.objects.get(id=id)
            return sponsor
        except Sponsor.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        sponsor = self.get_sponsor(id)
        serializer = SponsorSerializer(sponsor)
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        sponsor = self.get_sponsor(id)
        sponsor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id, format=None):
        sponsor = self.get_sponsor(id)
        serializer = SponsorSerializer(sponsor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        sponsor = self.get_sponsor(id)
        serializer = SponsorSerializer(sponsor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)