from django.db import models
from common.models import BaseModel


class Sponsor(BaseModel):
    nama = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'sponsor - {self.nama}'
    

class Acara(BaseModel):
    nama = models.CharField(max_length=200, unique=True)
    waktu_mulai = models.DateTimeField(help_text="Tanggal dan waktu mulai acara")
    waktu_selesai = models.DateTimeField(help_text="Tanggal dan waktu selesai acara")
    sponsor_list = models.ManyToManyField(Sponsor, through='SponsorAcara')

    def __str__(self):
        return (self.nama)
    

class SponsorAcara(BaseModel):
    PACKAGE_CHOICES = [
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
    ]

    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    acara = models.ForeignKey(Acara, on_delete=models.CASCADE)
    package = models.CharField(max_length=200, choices=PACKAGE_CHOICES)

    def __str__(self):
        return f'Sponsor {self.sponsor.nama} paket {self.package} untuk {self.acara.nama}'
    
    
    class Meta:
        unique_together = ['sponsor', 'acara']
    

class Materi(BaseModel):
    acara = models.ForeignKey(Acara, on_delete=models.CASCADE)
    judul = models.CharField(max_length=200)
    
    def __str__(self):
        return f'Pembicara {self.pembicara} untuk acara {self.acara.nama}'
    

class Pembicara(BaseModel):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nama}'


class PembicaraMateri(BaseModel):
    pembicara = models.CharField(max_length=200)
    materi = models.ForeignKey(Materi, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'pembicara - {self.pembicara}'
