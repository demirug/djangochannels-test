from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.views import View


class TestView(View):

    def get(self, request, *args, **kwargs):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)('test_channel', {"type": "log.msg", "message": "hello world"})
        return HttpResponse(200, "Okay")