from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import MatchInvitation

@shared_task
def send_invitation_email(invitation_id):
    invitation = MatchInvitation.objects.get(id=invitation_id)
    subject = f"New Match Invitation from {invitation.from_team.name}"
    message = f"Hello {invitation.to_team.owner.username},\n\n" \
              f"{invitation.from_team.name} has invited your team to a match.\n\n" \
              f"Visit the site to accept or reject the invitation."
    recipient = invitation.to_team.owner.email

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient])


@shared_task
def send_status_email(invitation_id,status):
    invitation = MatchInvitation.objects.get(id=invitation_id)
    subject = f"Match Status from {invitation.to_team.name}"
    message = f"Hello {invitation.from_team.owner.username},\n\n" \
              f"{invitation.to_team.name}  {status} your invite " \

    recipient = invitation.from_team.owner.email

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient])