from rest_framework import serializers
from user.models import User
import re

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={
            "required": "Password is required.",
            "min_length": "Password must have at least 8 symbols.",
        },
    )

    email = serializers.EmailField(
        error_messages={
            "required": "E-mail field is required.",
            "invalid": "Please enter a valid E-mail address.",
        }
    )

    class Meta:
        model = User
        fields = ('id', 'username','email','password')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def validate_password(self, value):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', value):
            raise serializers.ValidationError(
                "Password should consist of at least 8 symbols, including at least one uppercase letter, one number and one special character"
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class UserStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username')
        read_only_field = ("username",)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','email','team')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['team'] = instance.team.name if instance.team else None

        return representation