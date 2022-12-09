from django.urls import path

from apps.chat.consumers import ChatConsumer

urlpatterns = [
    path("chat/<str:room_name>/", ChatConsumer.as_asgi())
]