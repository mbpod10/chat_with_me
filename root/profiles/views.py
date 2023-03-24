from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import ChatRoomSerializer, MessageSerializer
from rest_framework.parsers import JSONParser
from .models import ChatRoom, Message

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

