from django.core.exceptions import ValidationError
from django.db import models
from rest_framework.exceptions import PermissionDenied

from final_project import settings
from team.models import Team



class Tournament(models.Model):
    organizers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='organized_tournaments')
    name = models.CharField(max_length=150,null=False,unique=True)
    teams = models.ManyToManyField(Team,related_name='tournaments')
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    stadium_place = models.CharField(max_length=100,null=False, blank=False)
    entry_fee = models.PositiveIntegerField(null=False, blank=False)
    teams_quantity = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return self.name




