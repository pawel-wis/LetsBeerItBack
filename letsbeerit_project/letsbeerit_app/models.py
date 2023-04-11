from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class AppUser(User):
    pass

class SocialGroup(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)