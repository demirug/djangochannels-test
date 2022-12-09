import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer


class AsyncChatConsumer(AsyncWebsocketConsumer):
    """Sending/receiving messages from group async"""

    async def connect(self):
        self.room_group_name = "chat_%s" % self.scope['url_route']['kwargs']['room_name']

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(self.room_group_name, {"type": "chat_message", "message": message})

    async def chat_message(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))


class SyncChatConsumer(WebsocketConsumer):
    """Sending/receiving messages from group sync"""
    def connect(self):
        self.room_group_name = "chat_%s" % self.scope['url_route']['kwargs']['room_name']

        async_to_sync(self.channel_layer.group_add) \
            (self.room_group_name, self.channel_name)

        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard) \
            (self.room_group_name, self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        async_to_sync(self.channel_layer.group_send) \
            (self.room_group_name, {"type": "chat_message", "message": message})

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"message": message}))


class MultipleGroupsSyncChatConsumer(WebsocketConsumer):
    """Sending/receiving messages from multiple groups"""
    groups = ['global', 'personal']

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        for group in self.groups:
            async_to_sync(self.channel_layer.group_send) \
                (group, {"type": "chat_message", "message": message})

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({"message": message}))
