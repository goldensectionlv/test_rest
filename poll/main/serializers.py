from rest_framework import serializers
from .models import Poll, Question, Answer, AnswerWithOneChoice, AnswerWithManyChoices


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'name', 'date_starts', 'date_ends', 'description']

    def save(self):
        poll_to_save = Poll(
            name=self.validated_data['name'],
            date_starts=self.validated_data['date_starts'],
            date_ends=self.validated_data['date_ends'],
            description=self.validated_data['description']
        )

        return poll_to_save


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type']

    def save(self):
        questions_for_poll = Question(
            question_text=self.validated_data['question_text'],
            question_type=self.validated_data['question_type']
        )
        return questions_for_poll


class AllPollsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'


class AllAnswersSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source='question.question_text', read_only=True)
    poll = serializers.CharField(source='poll.name', read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerWithOneChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerWithOneChoice
        fields = '__all__'


class AnswerWithManyChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerWithManyChoices
        fields = '__all__'


class QuestionSerializerNormal(serializers.ModelSerializer):
    poll = serializers.CharField(source='poll.name', read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
