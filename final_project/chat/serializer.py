from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    timestamp = serializers.ReadOnlyField()

    class Meta:
        model = Chat
        fields = ['id', 'match_invitation', 'sender', 'message', 'timestamp']