from django.urls import path, include

import sounds.views as views
from sounds.models import (Wavetable, ImpulseResponse, 
    LoopType, Sound, Loop, SoundKit, SoundKeyCode, KeyCode)
from rest_framework import serializers, viewsets, routers

class WavetableSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Wavetable
        fields = ['title', 'file', 'uuid']

class ImpulseResponseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ImpulseResponse
        fields = ['title', 'file', 'uuid']

class SoundSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sound
        fields = ['title', 'file', 'uuid']

class KeyCodeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = KeyCode
        fields = ['title', 'code']

class SoundKeyCodeSerializer(serializers.ModelSerializer):
    sound = SoundSerializer(read_only=True)
    key_code = KeyCodeSerializer(read_only=True)
    class Meta:
        model = SoundKeyCode
        fields = ['sound','key_code']

class SoundKitSerializer(serializers.ModelSerializer):
    sound_key_codes = SoundKeyCodeSerializer(read_only=True, many=True)
    class Meta:
        model = SoundKit
        fields = ['title', 'sound_key_codes']

class LoopTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoopType
        fields = ['title']

class LoopSerializer(serializers.HyperlinkedModelSerializer):
    loop_type = LoopTypeSerializer(read_only=True)
    class Meta:
        model = Loop
        fields = ['title', 'file', 'uuid', 'bpm', 'loop_type']

class SoundKitViewSet(viewsets.ModelViewSet):
    queryset = SoundKit.objects.all()
    serializer_class = SoundKitSerializer

class WavetableViewSet(viewsets.ModelViewSet):
    queryset = Wavetable.objects.all()
    serializer_class = WavetableSerializer

class ImpulseResponseViewSet(viewsets.ModelViewSet):
    queryset = ImpulseResponse.objects.all()
    serializer_class = ImpulseResponseSerializer

class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class LoopViewSet(viewsets.ModelViewSet):
    queryset = Loop.objects.all()
    serializer_class = LoopSerializer

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'soundkits', SoundKitViewSet)
router.register(r'wavetables', WavetableViewSet)
router.register(r'impulse_responses', ImpulseResponseViewSet)
router.register(r'single_samples', SoundViewSet)
router.register(r'loops', LoopViewSet)

app_name = "sounds"
urlpatterns = [
    path('', include(router.urls)),
    path("soundkit", view=views.SoundkitList.as_view(), name="soundkit"),
    path("soundkit/<int:pk>", view=views.SoundkitDetail.as_view(), name="view_soundkit"),
    path("soundkit/create", view=views.SoundkitCreate.as_view(), name="create_soundkit"),
    path("sound", view=views.sound_list_view, name="sound"),
]
