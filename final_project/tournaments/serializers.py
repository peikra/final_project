from django.core.cache import cache
from rest_framework import serializers
from tournaments.models import Tournament
from team.models import Team


class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ['id','name','organizers','start_date','end_date','stadium_place','entry_fee','teams_quantity','teams']
        read_only_fields = ['id','teams',]

    def create(self, validated_data):
        organizers = validated_data.pop('organizers', [])
        tournament = Tournament.objects.create(**validated_data)
        tournament.organizers.set(organizers)
        return tournament

    def to_representation(self, instance):
        cache_key = f"tournament_{instance.id}_representation"
        cached_representation = cache.get(cache_key)

        if cached_representation:
            return cached_representation

        representation = super().to_representation(instance)
        representation['organizers'] = [organizer.username for organizer in instance.organizers.all()]
        representation['teams'] = [team.name for team in instance.teams.all()]

        cache.set(cache_key, representation, 60 * 5)

        return representation

class AddTeamOnTournamentSerializer(serializers.ModelSerializer):
    team_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Tournament
        fields = ['team_id']

class LeaveTournamentSerializer(serializers.ModelSerializer):
    team_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Tournament
        fields = ['team_id']