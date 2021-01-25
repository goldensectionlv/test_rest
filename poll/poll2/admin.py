from django.contrib import admin
from poll2.models import *


# Register your models here.

class UserAnswerInline(admin.TabularInline):
    model = UserAnswer


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    readonly_fields = ('id', )


class QuestionInline(admin.TabularInline):
    model = Question


class PollAdmin(admin.ModelAdmin):
    model = Poll
    inlines = [QuestionInline, AnswerOptionInline, UserAnswerInline]
    readonly_fields = ('id', 'date_starts')


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [AnswerOptionInline]
    readonly_fields = ('id',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)