from django.contrib import admin
from .models import ProfileModel


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "avatar"]


admin.site.register(ProfileModel, ProfileAdmin)
