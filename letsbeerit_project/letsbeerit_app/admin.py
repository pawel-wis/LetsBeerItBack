from django.contrib import admin

# Register your models here.
from .models import AppUser, SocialGroup

admin.site.register(AppUser)
admin.site.register(SocialGroup)
