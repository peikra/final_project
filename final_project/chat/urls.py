from django.urls import path
from .views import ChatListView, ChatCreateView

urlpatterns = [
    path('api/match/<int:invitation_id>/chat/', ChatListView.as_view(), name='chat-list'),
    path('api/match/<int:invitation_id>/chat/send/', ChatCreateView.as_view(), name='chat-create'),
]