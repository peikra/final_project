from django.db import models
from rest_framework.exceptions import ValidationError
from final_project import settings


class Team(models.Model):
    name = models.CharField(max_length=255,unique=True)
    location = models.CharField(max_length=100,null=False)
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='owned_team'
    )
    logo = models.ImageField(upload_to='team_images/',null=True, blank=True)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def add_member(self, user):
        """
        Add a member to the team if they are not part of another team.
        """
        if user.team:
            raise ValidationError(f"User {user.username} is already in another team.")
        user.team = self
        user.save()

    def remove_member(self, user):
        """
        Remove a member from the team.
        """
        if user.team != self:
            raise ValidationError(f"User {user.username} is not a member of this team.")
        user.team = None
        user.save()


