from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class ProfileCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = [
            'email',
            'fio',
            'role',
        ]

    def create(self, validated_data):
        user = get_user_model().objects.create(username=validated_data['username'])
        user.set_password(User.objects.make_random_password())
        user.save()

        profile = Profile.objects.create(user=user)

        return profile
