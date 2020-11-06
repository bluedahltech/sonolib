from django.urls import path

from sounds.views import (
    sounds_json_view
)

app_name = "sounds"
urlpatterns = [
    path("", view=sounds_json_view, name="list"),
]
