from rest_framework import serializers
from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class AnswerOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOption
        fields = ['id', 'option_name']


class UserAnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.question_text')

    class Meta:
        model = UserAnswer
        fields = ['id', 'question', 'text_answer', 'answer_option', ]
