from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import LoginForm, SignupForm
from .models import ProfileModel


def user_logout(request):
    logout(request)
    return render(request, "account/logout.html")


def user_signup(request):
    if request.method == "GET":
        return render(request, "account/signup.html", {"form": SignupForm()})

    form = SignupForm(request.POST)

    if not form.is_valid():
        return render(
            request,
            "account/signup.html",
            {"error_message": form.errors.as_text(), "form": SignupForm()},
        )

    new_user = form.save(commit=False)
    new_user.set_password(form.cleaned_data["password_confirm"])
    new_user.save()
    ProfileModel.objects.create(user=new_user)

    # if not user:
    #     return render(
    #         request,
    #         "account/signup.html",
    #         {"error_message": "Not found. Try again.", "form": SignupForm()},
    #     )

    # if not user.is_active:
    #     return render(
    #         request,
    #         "account/signup.html",
    #         {"error_message": "Account isn't activated yet.", "form": SignupForm()},
    #     )

    return redirect("account:login")


def user_login(request):
    if request.method == "GET":
        return render(request, "account/login.html", {"form": LoginForm()})

    form = LoginForm(request.POST)

    if not form.is_valid():
        return render(
            request,
            "account/login.html",
            {"error_message": form.errors.as_text(), "form": LoginForm()},
        )

    user = authenticate(
        request,
        username=form.cleaned_data["username"],
        password=form.cleaned_data["password"],
    )

    if not user:
        return render(
            request,
            "account/login.html",
            {"error_message": "Not found. Try again.", "form": LoginForm()},
        )

    if not user.is_active:
        return render(
            request,
            "account/login.html",
            {"error_message": "Account isn't activated yet.", "form": LoginForm()},
        )

    login(request, user)

    return redirect("polls:index")
