from django.urls import path
from .views import SendInvitationView,ReceivedInvitationsView,UpdateInvitationStatusView

urlpatterns = [
    path('send-invitation/', SendInvitationView.as_view(), name='send_invitation'),
    path('get-invitations/', ReceivedInvitationsView.as_view(), name='get_invitations'),
    path('update-status/<int:pk>/',UpdateInvitationStatusView.as_view(),name='update-invitations')
]