from rest_framework.permissions import BasePermission
from .models import Team

class IsTeamOwner(BasePermission):
    """
    Custom permission to check if the request user is an organizer of the tournament.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

