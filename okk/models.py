import uuid
from django.db import models
from common.models import BaseModel

# jabatan constants
PI = 'PI'
BPH = 'BPH'
BPH_PJ = 'BPH-PJ'
BPH_WAPJ = 'BPH-WAPJ'

# Create your models here.

class Fakultas(BaseModel):
    nama = models.CharField(max_length=200, unique=True)
    nama_panggilan = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nama_panggilan
    


    