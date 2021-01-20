from django.http import HttpResponse
from django.urls import path
from .views import *


urlpatterns = [
    path('create_poll', create_poll),
    path('add_question', add_question),
    path('update_question', update_question),
    path('delete_question', delete_question),
    path('delete_all_questions', delete_all_questions),
    path('add_answer', add_answer),
    path('get_all_polls', get_all_polls),
    path('get_user_polls/<int:user_id>', get_user_polls),
    path('get_question/<int:question_id>', get_question),
    path('get_poll/<int:poll_id>', get_poll)

]
