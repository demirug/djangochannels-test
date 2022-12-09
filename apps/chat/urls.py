from django.urls import path
from . import views

urlpatterns = [
    path("", views.ChatView.as_view(), name="index"),
    path("<str:room_name>/", views.RoomView.as_view(), name="room")
]