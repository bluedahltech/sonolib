from django.shortcuts import render
from django.http import JsonResponse
from sounds.models import (Wavetable, ImpulseResponse, LoopType, 
            Instrument, Genre, Sound, Loop)

name_2_model = {
    'wavetable': Wavetable,
    'impulse': ImpulseResponse,
    'sound': Sound,
    'loop': Loop
}

def sounds_json_view(request):
    sound_category = request.GET.get('cat')
    search = request.GET.get('q', '')

    queryset = name_2_model[sound_category].objects.filter(title__icontains=search)
    results = []
    for sound in queryset:
        r = {}
        r['id'] = sound.uuid
        r['url'] = sound.file.url
        r['title'] = sound.title
        results.append(r)

    return JsonResponse({'results': results})
