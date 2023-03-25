from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatroomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chatroom_id = self.scope['url_route']['kwargs']['chatroom_id']
        await self.channel_layer.group_add(
            f'chatroom_{self.chatroom_id}',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f'chatroom_{self.chatroom_id}',
            self.channel_name
        )

    async def receive(self, text_data):
        message = json.loads(text_data)
        # handle message here

    async def chatroom_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))