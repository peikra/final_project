from django.contrib.auth.models import AbstractUser
from django.db import models
from team.models import Team


class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        related_name='members',
        null=True,
        blank=True
    )

    def leave_team(self):
        if self.team:
            self.team = None
            self.save()
            return True
        return False

    def __str__(self):
        return self.username