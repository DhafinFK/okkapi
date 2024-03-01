from django.db import models
from common.models import BaseModel


class Sponsor(BaseModel):
    nama = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'sponsor - {self.nama}'
    
    
class Pembicara(BaseModel):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nama}'
    

class Acara(BaseModel):
    nama = models.CharField(max_length=200, unique=True)
    waktu_mulai = models.DateTimeField(help_text="Tanggal dan waktu mulai acara")
    waktu_selesai = models.DateTimeField(help_text="Tanggal dan waktu selesai acara")
    sponsor_list = models.ManyToManyField(Sponsor, through='SponsorAcara')
    pembicara_list = models.ManyToManyField(Pembicara, related_name="mengisi")

    def __str__(self):
        return (self.nama)
    

class SponsorAcara(BaseModel):
    PACKAGE_CHOICES = [
        ('Platinum', 'Platinum'),
        ('Gold', 'Gold'),
        ('Silver', 'Silver'),
    ]

    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name="sponsorship")
    acara = models.ForeignKey(Acara, on_delete=models.CASCADE, related_name="sponsorship")
    package = models.CharField(max_length=200, choices=PACKAGE_CHOICES)

    def __str__(self):
        return f'Sponsor {self.sponsor.nama} paket {self.package} untuk {self.acara.nama}'
    
    
    class Meta:
        unique_together = ['sponsor', 'acara']
    
