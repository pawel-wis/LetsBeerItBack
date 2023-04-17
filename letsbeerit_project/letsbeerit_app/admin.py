from django.contrib import admin

# Register your models here.
from .models import AppUser, SocialGroup, SocialMembership

admin.site.register(AppUser)
admin.site.register(SocialGroup)
admin.site.register(SocialMembership)
