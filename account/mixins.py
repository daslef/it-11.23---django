from .models import ProfileModel
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin


class UserRelatedMixin(UserPassesTestMixin):
    permission_denied_message = "You are not authorized to view this page"

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        user_id = self.request.user.id
        user_profile = ProfileModel.objects.filter(user__id=user_id).get()
        path_id = int(self.request.path.split("/")[-1])
        return user_profile.id == path_id

    def handle_no_permission(self):
        return redirect("account:login")
