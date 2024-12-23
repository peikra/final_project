from rest_framework import serializers
from team.models import Team
from user.serializers import UserStateSerializer
from user.models import User


class TeamSerializer(serializers.ModelSerializer):
    owner = UserStateSerializer(read_only=True)
    members =  serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True
    )

    class Meta:
        model = Team
        fields = ['id','name','location','members','owner','wins','draws','losses','logo']
        read_only_fields = ['owner','wins','draws','losses']

    def create(self, validated_data):
        members = validated_data.pop('members', [])
        team = Team.objects.create(**validated_data)
        team.members.set(members)
        return team

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['members'] = [member.username for member in instance.members.all()]

        return representation

class UpdateTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('name','location')


class UpdateTeamWinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("wins",)

class UpdateTeamDrawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('draws',)

class UpdateTeamLosesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('losses',)

class UserTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id','name','wins','draws','losses','members','location')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['members'] = [member.username for member in instance.members.all()]

        return representation

class UpdateTeamMembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('members',)