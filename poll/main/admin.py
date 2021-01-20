from django.contrib import admin
from main.models import *


class AnswerAdmin(admin.ModelAdmin):
    model = Answer


class AnswerInline(admin.TabularInline):
    model = Answer


class AnswerWithOneChoiceInline(admin.TabularInline):
    model = AnswerWithOneChoice


class UserPollAdmin(admin.ModelAdmin):
    model = UserPoll
    inlines = [AnswerInline, ]
    readonly_fields = ('id',)


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ['poll', 'question_text', 'question_type']
    inlines = [AnswerInline, AnswerWithOneChoiceInline]
    readonly_fields = ('id',)


class QuestionInline(admin.TabularInline):
    model = Question


class PollAdmin(admin.ModelAdmin):
    model = Poll
    inlines = [QuestionInline, AnswerInline, AnswerWithOneChoiceInline]
    readonly_fields = ('id',)


class PollInline(admin.TabularInline):
    model = Poll


admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserPoll, UserPollAdmin)
