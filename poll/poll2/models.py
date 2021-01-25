from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CustomUser(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Anonymous')

    def __str__(self):
        return str(self.name) + ' id: ' + str(self.id)


class Poll(models.Model):
    name = models.CharField(max_length=255)
    date_starts = models.DateField(null=True)
    date_ends = models.DateField(null=True)
    description = models.TextField(max_length=1024)
    owner = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    TEXT = 'TEXT_ANSWER'
    OPTIONS_ANSWER = 'MANY_OPTIONS_ANSWER'
    QUESTION_TYPE = [
        (TEXT, TEXT),
        (OPTIONS_ANSWER, OPTIONS_ANSWER)
    ]
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPE, default=TEXT)
    question_periodic_number = models.IntegerField(default=1)

    def __str__(self):
        return str(self.question_text)


class AnswerOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    option_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.option_name)


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE)
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE, null=True)
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text_answer = models.CharField(max_length=1024, null=True, blank=True)
    answer_boolean = models.BooleanField(null=True, blank=True)
