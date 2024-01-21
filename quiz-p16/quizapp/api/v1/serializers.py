from rest_framework import serializers
from quizapp.models import QuizType, Answer, Result , User
from quizapp.models import Question


class QuizTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizType
        fields = ['id', 'name']

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['count_question'] = instance.question_set.count()
        return res



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['name', 'is_right']


class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizTypeSerializer(read_only=True)
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'quiz', 'name', 'answers']

    def get_answers(self, obj):
        obj = obj.answers.all()
        serializers = AnswerSerializer(obj, many=True)
        return serializers.data

    def to_representation(self, instance):
        res = super().to_representation(instance)
        request = self.context.get('request')
        print(request.user)
        if request:
            res['username'] = request.user.username
        return res



class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
