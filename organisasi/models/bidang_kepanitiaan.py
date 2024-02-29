from django.db import models
from common.models import BaseModel

PI = 'PI'
BPH = 'BPH'

BIDANG_KEPANITAAN_CHOICES = [
    (PI, 'Pengurus Inti'),
    (BPH, 'Badan Pengurus Harian'),
]


class BidangKepanitiaan(BaseModel):
    nama = models.CharField(max_length=200)
    bidang_panitia = models.CharField(max_length=200, choices=BIDANG_KEPANITAAN_CHOICES)

    def __str__(self):
        return self.nama