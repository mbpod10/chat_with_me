from django.urls import path
from profiles import views

urlpatterns = [
    path('chatrooms/', views.chatroom_list),
    path('messages/', views.message_list)
]

