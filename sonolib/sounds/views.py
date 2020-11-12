from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from sounds.models import (Wavetable, ImpulseResponse, LoopType, 
            Instrument, Genre, Sound, Loop, SoundKit,
             KeyCode, SoundKeyCode, FrequencyKit)

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import re

class FrequencykitDetail(DetailView): 
    model = FrequencyKit

class FrequencykitList(ListView): 
    model = FrequencyKit
    ordering = ['title']

class SoundkitDetail(DetailView): 
    model = SoundKit

class SoundkitList(ListView): 
    model = SoundKit
    ordering = ['title']

class FrequencykitCreate(LoginRequiredMixin, CreateView): 
    model = FrequencyKit
    def get(self, request):

        sounds = Sound.objects.all()
        key_codes = KeyCode.objects.all()

        context = {
         'sounds': sounds,
         'key_codes': key_codes
        }

        return render(request, 'sounds/frequencykit_create.html', context)

    def post(self, request):
        body = request.POST.dict()
        frequency_key_codes = []
        soundkit = SoundKit.objects.create(title=body['title'], created_by=request.user)
        for key in body:
            if 'keycode_' in key:
                keycode_id = int(re.search(r'\d+', key).group())
                keycode = KeyCode.objects.get(id=keycode_id)
                sound_id = body[key]
                sound = Sound.objects.get(uuid=sound_id)
                sound_key_code = SoundKeyCode.objects.create(key_code=keycode, sound=sound)
                soundkit.sound_key_codes.add(sound_key_code)
        
        soundkit.save()

        context = {
            'soundkit': soundkit
        }

        return render(request, 'sounds/soundkit_detail.html', context)

class SoundkitCreate(LoginRequiredMixin, CreateView): 
    model = SoundKit
    def get(self, request):

        sounds = Sound.objects.all()
        key_codes = KeyCode.objects.all()

        context = {
         'sounds': sounds,
         'key_codes': key_codes
        }

        return render(request, 'sounds/soundkit_create.html', context)

    def post(self, request):
        body = request.POST.dict()
        sound_key_codes = []
        soundkit = SoundKit.objects.create(title=body['title'], created_by=request.user)
        for key in body:
            if 'keycode_' in key:
                keycode_id = int(re.search(r'\d+', key).group())
                keycode = KeyCode.objects.get(id=keycode_id)
                sound_id = body[key]
                sound = Sound.objects.get(uuid=sound_id)
                sound_key_code = SoundKeyCode.objects.create(key_code=keycode, sound=sound)
                soundkit.sound_key_codes.add(sound_key_code)
        
        soundkit.save()

        context = {
            'soundkit': soundkit
        }

        return render(request, 'sounds/soundkit_detail.html', context)


def sound_list_view(request):
    return render('sound.html')
