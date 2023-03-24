from django.urls import path
from profiles import views

urlpatterns = [
    path('chatrooms/<int:chatroom_id>/users/', 
         views.ChatroomUserListView.as_view(), 
         name='chatroom_user_list'),
    path('chatrooms/', views.chatroom_list),
    path('messages/', views.message_list)
]

