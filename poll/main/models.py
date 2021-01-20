from django.db import models
from django.contrib.auth.models import User


class UserPoll(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, null=True, default='Anonymous')

    def __str__(self):
        return str(self.name) + ' ' + str(self.id)


class Poll(models.Model):
    name = models.CharField(max_length=255, null=True)
    date_starts = models.DateField(null=True, editable=False)
    date_ends = models.DateField(null=True)
    description = models.TextField(max_length=500, null=True)
    owner = models.OneToOneField(UserPoll, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    TEXT_ANSWER = 'TEXT_ANSWER'
    ONE_OPTION_ANSWER = 'ONE_OPTION_ANSWER'
    MANY_OPTIONS_ANSWER = 'MANY_OPTIONS_ANSWER'
    QUESTION_TYPE = [
        (TEXT_ANSWER, 'TEXT_ANSWER'),
        (ONE_OPTION_ANSWER, 'ONE_OPTION_ANSWER'),
        (MANY_OPTIONS_ANSWER, 'MANY_OPTIONS_ANSWER')
    ]
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255, choices=QUESTION_TYPE, default=TEXT_ANSWER)

    def __str__(self):
        return str(self.poll) + ' - ' + str(self.question_text)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer_question', on_delete=models.CASCADE)
    user_poll = models.ForeignKey(UserPoll, related_name='user_poll_rel', on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(Poll, related_name='answer_poll_rel', on_delete=models.CASCADE, null=True)
    answer_with_text = models.TextField(max_length=1000)

    def __str__(self):
        return str(self.question) + ' - ' + str(self.answer_with_text)


class AnswerWithOneChoice(models.Model):
    question = models.ForeignKey(Question, related_name='one_option_answer', on_delete=models.CASCADE)
    user_poll = models.ForeignKey(UserPoll, related_name='user_poll_choice_rel', on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(Poll, related_name='choice_answer_poll_rel', on_delete=models.CASCADE, null=True)
    answer = models.BooleanField(null=True)

    def __str__(self):
        return str(self.question)


class AnswerWithManyChoices(models.Model):
    question = models.ForeignKey(Question, related_name='many_option_answer', on_delete=models.CASCADE)
    user_poll = models.ForeignKey(UserPoll, related_name='user_poll_many_choice_rel', on_delete=models.CASCADE, null=True)
    poll = models.ForeignKey(Poll, related_name='many_choice_answer_poll_rel', on_delete=models.CASCADE, null=True)
    vote_one = models.BooleanField(null=True)
    vote_two = models.BooleanField(null=True)
    vote_three = models.BooleanField(null=True)
    vote_one_desc = models.CharField(max_length=255)
    vote_two_desc = models.CharField(max_length=255)
    vote_three_desc = models.CharField(max_length=255)

    def __str__(self):
        return str(self.question)
