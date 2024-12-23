from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from .models import Chat, MatchInvitation
from .serializer import ChatSerializer
from rest_framework.exceptions import PermissionDenied

@extend_schema(tags=['Chat'])
class ChatListView(generics.ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        match_invitation_id = self.kwargs['invitation_id']
        match_invitation = MatchInvitation.objects.get(id=match_invitation_id)


        if self.request.user != match_invitation.from_team.owner and self.request.user != match_invitation.to_team.owner:
            raise PermissionDenied("You do not have permission to view this chat.")

        return Chat.objects.filter(match_invitation=match_invitation).order_by('timestamp')


@extend_schema(tags=['Chat'])
class ChatCreateView(generics.CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        match_invitation_id = self.kwargs['invitation_id']
        match_invitation = MatchInvitation.objects.get(id=match_invitation_id)


        if self.request.user != match_invitation.from_team.owner and self.request.user != match_invitation.to_team.owner:
            raise PermissionDenied("You do not have permission to send messages in this chat.")
        if match_invitation.status != 'accepted':
            raise PermissionDenied("Chat is only available for accepted invitations.")

        serializer.save(sender=self.request.user, match_invitation=match_invitation)