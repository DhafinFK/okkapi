from django.contrib.auth.models import AbstractUser
from django.db import models
from mahasiswa.models import Mahasiswa

class CustomUser(AbstractUser):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')

    @property
    def is_panitia(self):
        return hasattr(self, 'panitia')
    
    @property
    def is_mentor(self):
        return hasattr(self, 'mentor')