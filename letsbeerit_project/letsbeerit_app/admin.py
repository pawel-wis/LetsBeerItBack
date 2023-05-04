from django.contrib import admin

# Register your models here.
from .models import AppUser, SocialGroup, SocialMembership, UserPin

admin.site.register(AppUser)
admin.site.register(SocialGroup)
admin.site.register(SocialMembership)
admin.site.register(UserPin)
