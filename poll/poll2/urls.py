from django.urls import path
from .views import *

urlpatterns = [
    path('create_poll', create_poll),
    path('update_poll', update_poll),
    path('delete_poll/<int:poll_id>', delete_poll),
    path('add_question', add_question),
    path('update_question', update_question),
    path('delete_question/<int:question_id>', delete_question),
    path('get_poll/<int:poll_id>', get_poll),
    path('get_all_polls', get_all_polls),
    path('add_answer', add_answer),
    path('add_answer_option', add_answer_option)
]
