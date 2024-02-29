from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    class Meta:
        abstract=True
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class SessionModel(models.Model):
    class Meta:
        abstract=True
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()