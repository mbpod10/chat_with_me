from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ChatRoomSerializer, MessageSerializer, UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from .models import ChatRoom, Message, ChatRoomUser
from django.contrib.auth.models import User

"""given a chatroom, show all messages as well as user information of message author"""
class ChatroomMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        chatroom_id = self.kwargs.get('chatroom_id')
        chatroom = ChatRoom.objects.get(id=chatroom_id)
        messages = Message.objects.filter(chatroom=chatroom).order_by("-created_at")
        return messages

"""display users that belong to a chatroom"""
class ChatroomUserListView(generics.ListAPIView):    
    serializer_class = UserSerializer

    def get_queryset(self):
      chatroom_id = self.kwargs.get('chatroom_id')
      chatroom = ChatRoom.objects.get(id=chatroom_id)
      chatroom_users = ChatRoomUser.objects.filter(chatroom=chatroom)
      user_ids = [chatroom_user.user.id for chatroom_user in chatroom_users]     
      return User.objects.filter(id__in=user_ids)      

    def list(self, request, *args, **kwargs):        
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def chatroom_list(request):
    if request.method == "GET":
        chatrooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        print(request.body)
        data = JSONParser().parse(request)
        serializer = ChatRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def message_list(request):
    if request.method == "GET":
        chatrooms = Message.objects.all()
        serializer = MessageSerializer(chatrooms, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        print(request.body)
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

