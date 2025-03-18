from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/%Y", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("account:profile", kwargs={"pk": self.id})
