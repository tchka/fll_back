from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLE = [
        (1, 'Заказчик'),
        (2, 'Копирайтер'),
    ]
    email = models.CharField("E-mail", max_length=1024)
    fio = models.CharField("ФИО", max_length=1024)
    role = models.PositiveSmallIntegerField(choices=USER_ROLE)
    REQUIRED_FIELDS = ["email", "fio", "role"]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER = [
        (1, 'Мужской'),
        (2, 'Женский'),
    ]
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=None, blank=True, null=True)


    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
