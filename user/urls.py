from django.urls import path
from .views import AudioWebSocketView


app_name = "user"
urlpatterns = [
    path('', AudioWebSocketView.as_view(), name='audio_websocket'),
]