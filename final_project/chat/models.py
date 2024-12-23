from django.db import models
from match.models import MatchInvitation
from user.models import User


class Chat(models.Model):
    match_invitation = models.ForeignKey(MatchInvitation, on_delete=models.CASCADE, related_name='chats')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"