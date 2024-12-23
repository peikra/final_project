from rest_framework import serializers
from .models import MatchInvitation
from team.serializers import TeamSerializer


class MatchSerializer(serializers.ModelSerializer):
    from_team = serializers.CharField(source='from_team.name',read_only=True)

    class Meta:
        model = MatchInvitation
        fields = ['id','from_team','to_team','status']
        read_only_fields = ['from_team','status']



class GetMatchIvitationSerializer(serializers.ModelSerializer):
    from_team = serializers.CharField(source='from_team.name',read_only=True)

    class Meta:
        model = MatchInvitation
        fields = ['id','from_team','status']

class UpdateMatchInvitiationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchInvitation
        fields = ['status']