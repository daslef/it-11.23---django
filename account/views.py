from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def user_login(request):
    if request.method == "GET":
        return render(request, "account/login.html")

    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    print(user, user.is_active)

    if not user:
        return render(
            request, "account/login.html", {"error_message": "Not found. Try again."}
        )

    if not user.is_active:
        return render(
            request,
            "account/login.html",
            {"error_message": "Account isn't activated yet."},
        )

    login(request, user)

    return redirect("polls:index")
