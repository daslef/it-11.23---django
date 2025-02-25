from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    recent_questions = models.Question.objects.all().order_by("-pub_date")[:2]
    return render(request, "polls/index.html", {"recent_questions": recent_questions})


def detail(request, question_id):
    question = get_object_or_404(models.Question, id=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(models.Question, id=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(models.Question, id=question_id)
    try:
        selected_choice_id = request.POST.get("choice")
        selected_choice = question.choice_set.get(id=selected_choice_id)
    except (KeyError, models.Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "No choice selected"},
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
