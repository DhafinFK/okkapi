from django.db import models
from common.models import BaseModel

# Create your models here.

class Acara(BaseModel):
    nama = models.CharField(max_length=200, unique=True)
    waktu_mulai = models.DateTimeField(help_text="Tanggal dan waktu mulai acara")
    waktu_selesai = models.DateTimeField(help_text="Tanggal dan waktu selesai acara")

    def __str__(self):
        return (self.nama)