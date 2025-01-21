import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user: User = self.scope['user']

        if user.is_anonymous:
            await self.close(code=4001)  # Close for unauthenticated users
            return

        self.room_name = 'chat_room'
        self.room_group_name = f"main_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()



    async def disconnect(self, close_code):
        # Логика для отключения
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправим сообщение всем клиентам в группе
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Отправим сообщение WebSocket клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))