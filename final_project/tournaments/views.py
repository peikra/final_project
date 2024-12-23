from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from team.serializer_utils import SerializerFactory
from tournaments.serializers import TournamentSerializer
from tournaments.models import Tournament
from tournaments.serializers import AddTeamOnTournamentSerializer
from team.models import Team
from .permissions import IsTournamentOrganizer
from .serializers import LeaveTournamentSerializer


@extend_schema(tags=["Tournaments"])
class CreateTournamentViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerFactory(
        create=TournamentSerializer,
        default=TournamentSerializer,

    )
    queryset = Tournament.objects.all()

    def get_permissions(self):
        if self.action in ("update", "destroy"):
            permission_classes = [IsAuthenticated, IsTournamentOrganizer]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        start_date = self.request.data['start_date']
        end_date = self.request.data['end_date']

        if start_date > end_date:
            raise ValidationError("Start date cannot be after or equal to the end date.")
        serializer.save()

@extend_schema(tags=['Tournaments'])
class AddTeamOnTournamentView(generics.UpdateAPIView):
    serializer_class = AddTeamOnTournamentSerializer
    queryset = Tournament.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        tournament = self.get_object()
        team_id = request.data.get('team_id')

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"error": "Team not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user.owned_team != team:
            return Response({"error": "You do not own this team."}, status=status.HTTP_403_FORBIDDEN)

        if team in tournament.teams.all():
            return Response({"error": "Your team is already add on tournament."}, status=status.HTTP_403_FORBIDDEN)

        if tournament.teams_quantity>0:
            tournament.teams.add(team)
            tournament.teams_quantity -= 1
            tournament.save()
            return Response({"success": f"Team '{team.name}' added to tournament '{tournament.name}'."})

        return Response({"all team is already registered on tournament"},status=status.HTTP_403_FORBIDDEN)


@extend_schema(tags=['Tournaments'])
class LeaveTournamentView(generics.UpdateAPIView):
    serializer_class = LeaveTournamentSerializer
    queryset = Tournament.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        tournament = self.get_object()
        team_id = request.data.get('team_id')

        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"error": "Team not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.user != team.owner:
            return Response({"error": "You do not own this team."}, status=status.HTTP_403_FORBIDDEN)


        if team not in tournament.teams.all():
            return Response({"error": "This team is not part of the tournament."}, status=status.HTTP_400_BAD_REQUEST)

        tournament.teams.remove(team)
        tournament.teams_quantity+=1
        tournament.save()

        return Response({"success": f"Team '{team.name}' has been removed from tournament '{tournament.name}'."}, status=status.HTTP_200_OK)