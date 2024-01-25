from django.test import TestCase
from django.urls import reverse

from quizapp.api.v1.serializers import QuizTypeSerializer
from quizapp.models import QuizType


# Create your tests here.

class TestQuizType(TestCase):

    def setUp(self):
        self.quiz_type = QuizType.objects.create(name='Test check work')


    def test_create(self):
        serializer = QuizTypeSerializer(self.quiz_type).data
        print(serializer)


class TestQuizTypeView(TestCase):
    def setUp(self) -> None:
        self.quiz_type1 = QuizType.objects.create(name='Test 1')
        self.quiz_type2 = QuizType.objects.create(name='Test 2')

        self.url = reverse('quiz_types')


    def test_get(self):
        quiz_types = QuizType.objects.all()
        serializers = QuizTypeSerializer(quiz_types, many=True)
        print(serializers)




