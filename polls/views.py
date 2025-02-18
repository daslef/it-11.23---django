from django.http import HttpResponse, Http404
from django.shortcuts import render
from . import models


def index(request):
    recent_questions = models.Question.objects.all().order_by("-pub_date")[:2]
    return render(request, "polls/index.html", {"recent_questions": recent_questions})


def detail(request, question_id):
    try:
        question = models.Question.objects.get(id=question_id)
    except models.Question.DoesNotExist:
        raise Http404("Question with that id does not exist")

    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question {}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
