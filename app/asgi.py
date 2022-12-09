"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from django.core.asgi import get_asgi_application
from django.urls import path

from app.ws_urls import urlpatterns as websocket_urlpatterns
from apps.channelsend.consumers import ChannelTest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(URLRouter([path("ws/", URLRouter(websocket_urlpatterns))])),
    "channel": ChannelNameRouter({
        "test_channel": ChannelTest.as_asgi(),
    }),
})
