from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/%Y-%M", null=True, blank=True)
