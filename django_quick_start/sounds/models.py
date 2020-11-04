from __future__ import unicode_literals
import uuid

from django.db import models

# Create your models here.

class Wavetable(models.Model):
    title = models.CharField(max_length=250)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    wavetable = models.FileField()
    


