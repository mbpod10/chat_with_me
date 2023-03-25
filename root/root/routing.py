from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from root.consumers import ChatroomConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/chatroom/<int:chatroom_id>/', ChatroomConsumer.as_asgi())
    ])
})