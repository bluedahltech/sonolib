from __future__ import unicode_literals
import uuid

from django.db import models
from sonolib.users.models import User

class Wavetable(models.Model):
    title = models.CharField(max_length=250)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()

class ImpulseResponse(models.Model):
    title = models.CharField(max_length=250)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()

class LoopType(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

class Instrument(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

class Genre(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

class Sound(models.Model):
    title = models.CharField(max_length=250)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    file = models.FileField()
    key = models.CharField(max_length=100)

class Loop(models.Model):
    title = models.CharField(max_length=250)
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    loop_type = models.ForeignKey(LoopType, on_delete=models.CASCADE)
    file = models.FileField()
    key = models.CharField(max_length=100)
    bpm = models.IntegerField()


class KeyCode(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=250)

class SoundKeyCode(models.Model):
    sound = models.ForeignKey(Sound, on_delete=models.CASCADE)
    key_code = models.ForeignKey(KeyCode, on_delete=models.CASCADE)

class SoundKit(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sound_key_codes = models.ManyToManyField('SoundKeyCode')

class FrequencyKeyCode(models.Model):
    frequency = models.DecimalField(max_digits=20, decimal_places=2)
    key_code = models.ForeignKey(KeyCode, on_delete=models.CASCADE)

class FrequencyKit(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sound_key_codes = models.ManyToManyField('FrequencyKeyCode')