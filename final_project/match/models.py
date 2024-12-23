from django.db import models
from team.models import Team


class MatchInvitation(models.Model):
    from_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='sent_invitations')
    to_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='received_invitations')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], default='pending')

    def __str__(self):
        return f"{self.from_team} -> {self.to_team} ({self.status})"