from rest_framework.permissions import BasePermission
from .models import Tournament

class IsTournamentOrganizer(BasePermission):
    """
    Custom permission to check if the request user is an organizer of the tournament.
    """
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Tournament):
            return request.user in obj.organizers.all()
        return False
