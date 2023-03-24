from django.contrib import admin
from .models import ChatRoom, Message, ChatRoomUser, Notification

admin.site.register(ChatRoom)
admin.site.register(Message)
admin.site.register(ChatRoomUser)
admin.site.register(Notification)
# Register your models here.
