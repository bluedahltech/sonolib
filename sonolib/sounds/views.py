from django.shortcuts import render
from django.http import JsonResponse
from .models import (Wavetable, ImpulseResponse, LoopType, 
            Instrument, Genre, Sound, Loop)

name_2_model = {
    'wavetable': Wavetable,
    'impulse': ImpulseResponse,
    'sound': Sound,
    'loop': Loop
}

def sounds_json_view(request):
    sound_category = request.GET.get('cat')
    search = request.GET.get('q')


