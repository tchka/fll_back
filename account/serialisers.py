from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

        read_only_fields = [
            'user',
        ]


#
# class ProfileCreateSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user.username')
#
#     class Meta:
#         model = Profile
#         fields = [
#             'gender',
#         ]
#
#     def create(self, validated_data):
#         user = get_user_model().objects.create(username=validated_data['username'])
#         user.set_password(User.objects.make_random_password())
#         user.save()
#
#         profile = Profile.objects.create(user=user)
#
#         return profile


class UserRetrieveSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True, many=False)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'fio',
            'role',
            'profile',
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False, many=False)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'fio',
            'role',
            'profile',
        ]
        read_only_fields = [
            'username',
            'email',
            'role',
        ]

    def update(self, instance, validated_data):
        print(validated_data['profile'].get('gender'))
        profile, created = Profile.objects.update_or_create(user=instance, defaults={
            'gender': validated_data['profile'].get('gender')
        })
        instance.fio = validated_data.get('fio', instance.fio)

        instance.save()
        return instance
