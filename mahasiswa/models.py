from django.db import models
from common.models import BaseModel
from okk.models import Fakultas
from organisasi.models import BidangKepanitiaan
from kelompok.models import Kelompok

# jabatan constants
PI = 'PI'
BPH_PJ = 'BPH-PJ'
BPH_WAPJ = 'BPH-WAPJ'
STAFF = 'STAFF'

JABATAN_CHOICES = [
    (PI, 'Pengurus Inti'),
    (BPH_PJ, 'BPH - Penanggung Jawab'),
    (BPH_WAPJ, 'BPH - Wakil Penanggung Jawab'),
    (STAFF, 'Staff'),
]

# Create your models here.

class Mahasiswa(BaseModel):
    nama = models.CharField(max_length=200)
    npm = models.CharField(max_length=200, unique=True)
    fakultas = models.ForeignKey(Fakultas, on_delete=models.PROTECT)
    angkatan = models.PositiveIntegerField(default=2023)

    def __str__(self):
        return f'{self.nama} ({self.npm}) dari {self.fakultas}'
    
    
class Panitia(BaseModel):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE)
    jabatan = models.CharField(max_length=200, choices=JABATAN_CHOICES)
    bidang = models.ForeignKey(BidangKepanitiaan, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mahasiswa.nama} ({self.jabatan}) - {self.bidang.nama}'


class Mentor(BaseModel):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE)
    kelompok = models.OneToOneField(Kelompok, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.mahasiswa.nama} - {self.kelompok.nomor}'


class Mentee(BaseModel):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE)
    kelompok = models.ForeignKey(Kelompok, on_delete=models.CASCADE)
    jalur_masuk = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.mahasiswa.nama} - {self.kelompok.nomor}'