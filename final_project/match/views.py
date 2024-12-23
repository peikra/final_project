from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import MatchInvitation
from .serializer import MatchSerializer, GetMatchIvitationSerializer, UpdateMatchInvitiationSerializer
from team.models import Team
from .tasks import send_invitation_email, send_status_email


@extend_schema(tags=['Match'])
class SendInvitationView(generics.CreateAPIView):
    queryset = MatchInvitation.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        from_team = get_object_or_404(Team, owner=self.request.user)
        to_team = serializer.validated_data.get('to_team')

        if from_team==to_team:
            raise Exception("you cant play against yourself")

        if not to_team:
            raise Exception(
                {"detail": "Invalid target team."}
            )


        if MatchInvitation.objects.filter(from_team=from_team, to_team=to_team).exists():
            raise PermissionDenied("this invitation is already exist")

        invitation = serializer.save(from_team=from_team, to_team=to_team)
        send_invitation_email(invitation.id)

        return Response(
            {"detail": "Invitation sent successfully."},
            status=status.HTTP_201_CREATED
        )



@extend_schema(tags=['Match'])
class ReceivedInvitationsView(generics.ListAPIView):
    serializer_class = GetMatchIvitationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_teams = Team.objects.filter(owner=self.request.user)
        return MatchInvitation.objects.filter(to_team__in=user_teams)

@extend_schema(tags=['Match'])
class UpdateInvitationStatusView(generics.UpdateAPIView):
    queryset = MatchInvitation.objects.all()
    serializer_class = UpdateMatchInvitiationSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        invitation = super().get_object()

        if invitation.to_team.owner != self.request.user:
            raise PermissionDenied("You do not have permission to update this invitation.")
        status = self.request.data['status']
        send_status_email(invitation.id,status)
        return invitation