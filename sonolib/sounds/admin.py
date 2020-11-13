from django.contrib import admin

from .models import (Wavetable, ImpulseResponse, LoopType,
                Instrument, Genre, Sound, Loop, FrequencyKit)

# Register your models here.
@admin.register(Wavetable)
class WavetableAdmin(admin.ModelAdmin):
    list_display = ["title", "uuid"]
    pass

@admin.register(ImpulseResponse)
class ImpulseResponseAdmin(admin.ModelAdmin):
    list_display = ["title", "uuid"]
    pass

@admin.register(LoopType)
class LoopTypeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    pass

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ["title"]
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["title"]
    pass

@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    list_display = ["title", "uuid"]
    pass

@admin.register(Loop)
class LoopAdmin(admin.ModelAdmin):
    list_display = ["title", "uuid"]
    pass

@admin.register(FrequencyKit)
class FrequencyKitAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
    pass
