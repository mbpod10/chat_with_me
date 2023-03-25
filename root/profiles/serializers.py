from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from .models import ChatRoom, Message, ChatRoomUser, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')

class ChatRoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChatRoom
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'text', 'created_at', 'user']

    def get_user(self, obj):
        user = obj.user
        return {
            'username': user.username,
            'firstname': user.first_name,
            'lastname': user.last_name
        }

class ChatRoomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChatRoomUser
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields = '__all__'