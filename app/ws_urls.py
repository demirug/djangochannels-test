from django.urls import path

from apps.chat.consumers import SyncChatConsumer

urlpatterns = [
    path("chat/<str:room_name>/", SyncChatConsumer.as_asgi())
]