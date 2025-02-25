import datetime
from django.test import TestCase
from django.utils import timezone

from . import models


class QuestionModelTests(TestCase):
    def test_was_published_works_only_for_previous_dates(self):
        time = timezone.now() + datetime.timedelta(days=1)
        future_question = models.Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_returns_false_on_older_polls(self):
        time = timezone.now() - datetime.timedelta(days=5)
        old_question = models.Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_returns_true_on_recent_polls(self):
        time = timezone.now() - datetime.timedelta(days=4)
        recent_question = models.Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
