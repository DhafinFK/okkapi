from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FakultasSerializer
from django.http import HttpResponse, Http404
from .models import *
from organisasi.models import BidangKepanitiaan
from custom_auth.permissions import IsSuperUser

# Create your views here.

class FakultasList(APIView):
    """
    List semua fakultas dan create fakultas baru
    """
    permission_classes = [IsSuperUser]

    def get(self, requesst, format=None):
        fakultas = Fakultas.objects.all()
        serializer = FakultasSerializer(fakultas, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = FakultasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FakultasDetail(APIView):
    """
    Detail, buat, update fakultas tertentu
    """
    permission_classes = [IsSuperUser]

    def get_fakultas(self, name):
        try:
            fakultas = Fakultas.objects.get(nama_panggilan=name)
            return fakultas
        except Fakultas.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        fakultas = self.get_fakultas(name)
        serializer = FakultasSerializer(fakultas)
        return Response(serializer.data)
    
    def delete(self, request, name, format=None):
        fakultas = self.get_fakultas(name)
        fakultas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, name, format=None):
        fakultas = self.get_fakultas(name)
        serializer = FakultasSerializer(fakultas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, name, format=None):
        fakultas = self.get_fakultas(name)
        serializer = FakultasSerializer(fakultas, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# class AcaraDetail(APIView):
#     def get(self, request, )

def create_initial_fakultas(request):
    lineline = """Fakultas_Hukum&FH
Fakultas_Ilmu_Administrasi&FIA
Fakultas_Ilmu_Pengetahuan_Budaya&FIB
Fakultas_Ekonomi_dan_Bisnis&FEB
Fakultas_Ilmu_Keperawatan&FIK
Fakultas_Ilmu_Komputer&FASILKOM
Fakultas_Ilmu_Sosial_dan_Ilmu_Politik&FISIP
Fakultas_Kedokteran&FK
Fakultas_Kedokteran_Gigi&FKG
Fakultas_Kesehatan_Masyarakat&FKM
Fakultas_Matematika_dan_Ilmu_Pengetahuan_Alam&FMIPA
Fakultas_Psikologi&PSIKO
Fakultas_Teknik&FT
Program_Pendidikan_Vokasi&VOKASI"""
    lines = lineline.split('\n')
    for line in lines:
        line = line.strip('\n')
        line = line.split('&')
        line[0] = line[0].replace("_", " ")

        Fakultas.objects.create(nama=line[0], nama_panggilan=line[1])
    
    return HttpResponse('berhasil menambahkan fakul silahkan cek')


def create_bidang_kepanitiaan(reqeust):
    # bidang PI constants
    PO = 'PO' 
    VPO_INTERNAL = 'VPOI'   
    VPO_EKSTERNAL = 'VPOE'
    SEKRETARIS = 'Sekretaris'
    CONTROLLER = 'Controller' 
    TREASURER = 'Treasurer'
    KOOR_ACARA = 'koor-acara' 
    SARANA_PRASARANA = 'SNP'
    OPERASIONAL = 'OP' 
    MATERI_MENTOR = 'MnM'
    KREATIF = 'Kreatif'
    RELASI = 'Relasi'

    # bidang BPH constants
    PROJECT = 'Project'
    SPONSORSHIP = 'Sponsorship'
    SEKRE = 'Kesekretariatan'
    PSDM = 'PSDM'
    ACARA_PUNCCAK = 'Acara-Puncak'
    EKSPLORASI = 'Eksplorasi'
    TRANSPORT_KONSUM = 'Transportasi-Konsumsi'
    PERIZINAN = 'Perizinan'
    LOGISTIK = 'Logistik'
    KEAMANAN = 'Keamanan'
    MEDIS = 'Medis'
    MEDIA = 'Media Informasi'
    KELEMBAGAAN = 'Kelembagaan'
    MATERI = 'Materi'
    MENTOR = 'Mentor'
    MEDPAR = 'Media-Partner'
    IT = 'IT' 
    BROADCAST = 'Broadcast'
    DEKOR_WARDROBE = 'Dekorasi-Wardrobe' 
    VISDES_DOKUM = 'VisDes-Dokumentasi'

    BIDANG_PI_CHOICES = [
        (PO, 'Project Officer'), 
        (VPO_INTERNAL, 'Vice Project Officer Internal'), 
        (VPO_EKSTERNAL, 'Vice Project Officer Eksternal'), 
        (SEKRETARIS, 'Sekretaris'), 
        (CONTROLLER, 'Controller'), 
        (TREASURER, 'Treasurer'), 
        (KOOR_ACARA, 'Koordinator Acara'), 
        (SARANA_PRASARANA, 'Sarana dan Prasarana'), 
        (OPERASIONAL, 'Operasional'), 
        (MATERI_MENTOR, 'Materi'), 
        (KREATIF, 'Kreatif'), 
        (RELASI, 'Relasi'),
    ]

    BIDANG_BPH_CHOICES = [
        (PROJECT, 'Project'), 
        (SPONSORSHIP, 'Sponsorship'), 
        (SEKRE, 'Kesekretariatan'), 
        (PSDM, 'PSDM'), 
        (ACARA_PUNCCAK, 'Acara Puncak'), 
        (EKSPLORASI, 'Ekspolarsi'), 
        (TRANSPORT_KONSUM, 'Transportasi dan Konsumsi'), 
        (PERIZINAN, 'Perizinan'), 
        (LOGISTIK, 'Logistik'), 
        (KEAMANAN, 'Keamanan'), 
        (MEDIS, 'Medis'), 
        (MEDIA, 'Media'), 
        (KELEMBAGAAN, 'Kelembagaan'), 
        (MATERI, 'Materi'), 
        (MENTOR, 'Mentor'), 
        (MEDPAR, 'Media Partner'), 
        (IT, 'IT'), 
        (BROADCAST, 'Broadcast'), 
        (DEKOR_WARDROBE, 'Dekor dan Wardrobe'), 
        (VISDES_DOKUM, 'Visual Design dan Dokumentasi'),
    ]

    for tups in BIDANG_PI_CHOICES:
        BidangKepanitiaan.objects.create(nama=tups[1], bidang_panitia='PI')

    return HttpResponse('berhasil membuat bidang-bidang silahkan dilihat')