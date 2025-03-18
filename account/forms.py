from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Password Repeat"
    )

    def clean_password_confirm(self):
        cleaned = self.cleaned_data
        if cleaned["password"] != cleaned["password_confirm"]:
            raise forms.ValidationError("Password doesn't match")
        return cleaned["password_confirm"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ["user", "avatar"]
