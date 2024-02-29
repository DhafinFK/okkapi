from django.db import models
from common.models import BaseModel, SessionModel

# Create your models here.


class Kelompok(BaseModel):
    nomor = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"okk {self.nomor}"
    