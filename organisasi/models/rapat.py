from common.models import SessionModel
from django.db import models
from . import BidangKepanitiaan

class Rapat(SessionModel):
    bidang = models.ForeignKey(
        BidangKepanitiaan, 
        on_delete=models.CASCADE, 
        related_name="rapat"
    )

    attendees = models.ManyToManyField(
        "mahasiswa.Panitia",
        related_name="attended_sessions",
        blank=True,
    )
    
    def __str__(self):
        return f'Rapat bidang {self.bidang.nama} tanggal {self.date}'