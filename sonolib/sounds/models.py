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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Instrument(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Genre(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

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

# SoundKit idea, need to map out further  
# class SoundKit(models.Model):
#     title = models.CharField(max_length=250)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(User)
#     sounds = models.ForeignKey(Sound)

# class Note(models.Model):
#     title = models.CharField(max_length=250)

# class NoteSound(models.Model):
#     sound = models.ForeignKey(Sound)
#     note = models.ForeignKey(Note)