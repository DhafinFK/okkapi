from common.models import SessionModel
from django.db import models
from . import Kelompok
from mahasiswa.models import Mentee

class MentoringSession(SessionModel):
    kelompok = models.ForeignKey(
        Kelompok, 
        on_delete=models.CASCADE, 
        related_name="mentoring_sessions"
    )

    attendees = models.ManyToManyField(
        Mentee, 
        related_name="attended_sessions", 
        blank=True,
    )
    
    def __str__(self):
        return f'session kelompok {self.kelompok.nomor} tanggal {self.date}'