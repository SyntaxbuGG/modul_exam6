from django.test import TestCase

from quizapp.api.v1.serializers import QuizTypeSerializer
from quizapp.models import QuizType


# Create your tests here.

class TestQuizType(TestCase):

    def setUp(self):
        self.quiz_type = QuizType.objects.create(name='Test check work')


    def test_create(self):
        serializer = QuizTypeSerializer(self.quiz_type).data
        print(serializer)