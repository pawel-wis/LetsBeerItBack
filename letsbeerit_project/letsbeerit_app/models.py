from pyexpat import model

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserPin(models.Model):
    alt_name = models.CharField(max_length=30, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.user.username + " pinned at " + str(self.latitude) + ", " + str(self.longitude)


class AppUser(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    user_pin = models.OneToOneField(UserPin, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username


class SocialGroup(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name


APP_USERS_GROUP_ROLES = (("member", "admin"),)


class SocialMembership(models.Model):
    class Meta:
        unique_together = [["appuser", "socialgroup"], ]

    appuser = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="+")
    socialgroup = models.ForeignKey(SocialGroup, on_delete=models.CASCADE, related_name="+")
    role_user_in_group = models.CharField(max_length=10, choices=APP_USERS_GROUP_ROLES,
                                          default=APP_USERS_GROUP_ROLES[0])

    def __str__(self):
        return self.appuser.username + " is " + self.role_user_in_group + " in " + self.socialgroup.name
