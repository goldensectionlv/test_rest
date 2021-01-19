from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import *
from .models import *


# {"name":"poll","date_starts":"2021-01-21","date_ends":"2021-01-22","description":"description of poll"}

# {"poll": {"name": "poll", "date_starts": "2021-01-21", "date_ends": "2021-01-22", "description": "description of poll"}}

# упрощенная версия авторизации
def get_user_id_or_create(user_id):
    try:
        user_data = UserPoll.objects.get(id=user_id)
    except:
        UserPoll.objects.get_or_create(id=user_id)
        user_data = UserPoll.objects.get(id=user_id)
    return user_data


# poll = {
#     "poll": {"name": "poll", "date_starts": "2021-01-21", "date_ends": "2021-01-22",
#              "description": "description of poll"},
#     "questions": {"question_text": "question_text", "question_type": "TEXT_ANSWER"}
# }

'''CRUD'''


# Создание опроса с изначальными вопросами
@api_view(['POST'])
def create_poll(request):
    poll_object = None
    question_object = None
    poll_serializer = PollSerializer(data=request.data['poll'])
    if poll_serializer.is_valid():
        # сохраняю тут и таким образом для того, чтобы получить автоматически сгенерированный id
        poll_object = Poll.objects.create(**poll_serializer.validated_data)
        poll_object.save()
        print('poll_yes')
    else:
        print('poll no')

    question_serializer = QuestionSerializer(data=request.data['questions'])
    if question_serializer.is_valid():
        print('yes', question_serializer.data)
        question_object = Question.objects.create(**question_serializer.validated_data, poll=poll_object)
        question_object.save()

    else:
        print('no')
    return Response(poll_serializer.data)


poll_questions11 = {
    "poll_id": 85,
    "questions": "question",
    "question_type": "TEXT_ANSWER"
}


# Добавление вопроса
@api_view(['POST'])
def add_question(request):
    poll_id = request.data['poll_id']
    question = request.data['questions']
    question_type = request.data['question_type']

    if not Question.objects.filter(poll_id=poll_id, question_text=question).exists():
        Question.objects.create(poll_id=poll_id, question_text=question, question_type=question_type)
    else:
        print('question already exists')

    return Response('ok')


for_update_question = {
    "poll_id": 85,
    "question_old": "question",
    "question_new": "question111",
    "question_type": "TEXT_ANSWER"
}


#  Изменение данных вопроса
@api_view(['POST'])
def update_question(request):
    poll_id = request.data['poll_id']
    question_old = request.data['question_old']
    question_new = request.data['question_new']
    question_type = request.data['question_type']

    # Get-запрос внутри для того, чтобы не вызвать ошибку, если вопроса не существует
    if Question.objects.filter(poll_id=poll_id, question_text=question_old).exists():
        question_object = Question.objects.get(poll_id=poll_id, question_text=question_old)
        question_object.question_text = question_new
        question_object.question_type = question_type
        question_object.save()

    return Response('ok')


# Удаление конкретного вопроса
# @api_view(['POST'])
# def delete_question(request):
#     poll_id = request.data['poll_id']
#     question = request.data['questions']
#
#     if Question.objects.filter(poll_id=poll_id, question_text=question).exists():
#         Question.objects.get(poll_id=poll_id, question_text=question).delete()
#         print('deleted')
#     else:
#         print('does not exist')
#
#     return Response('ok')


# Удаление всех вопросов
@api_view(['POST'])
def delete_all_questions(request):
    poll_id = request.data['poll_id']
    question = Question.objects.filter(poll_id=poll_id)

    # Проверка на наличие вопросов
    if len(question) > 0:
        for i in range(len(question)):
            question[i].delete()
    else:
        print('список вопросов пуст')

    return Response('ok')


'''CRUD END'''

'''USER FUNCTIONAL'''

for_add_answer = {
    "poll_id": 87,
    "question": "one",
    "answer": "жил был хуй",
    "question_type": "TEXT_ANSWER",
    "user_id": "1234"
}


@api_view(['POST'])
def add_answer(request):
    poll_id = request.data['poll_id']
    question = request.data['question']
    answer = request.data['answer']
    question_type = request.data['question_type']

    user_data = get_user_id_or_create(user_id=request.data['user_id'])

    if Question.objects.filter(poll_id=poll_id, question_text=question).exists():
        question_object = Question.objects.get(poll_id=poll_id, question_text=question)
        print(question_object)
        Answer.objects.create(question=question_object, answer_with_text=answer, user_poll=user_data, poll_id=poll_id)
    else:
        print('question does not exist')

    return Response('ok')


@api_view(['GET'])
def get_all_polls(request):
    polls = Poll.objects.all()

    if len(polls) > 1:
        serializer = AllPollsSerializer(polls, many=True)
    else:
        serializer = AllPollsSerializer(polls)

    return Response(serializer.data)


for_get_user_polls = {
    "user_id": "1234"
}


@api_view(['GET'])
def get_user_polls(request, user_id):
    user_answers = Answer.objects.filter(user_poll=user_id)

    final = []
    polls_for_final = []
    for i in range(len(user_answers)):
        if user_answers[i].poll not in polls_for_final:
            polls_for_final.append(user_answers[i].poll)

    for i in range(len(polls_for_final)):
        polls = []
        answers = []
        for z in range(len(user_answers)):
            if user_answers[z].poll == polls_for_final[i]:
                answers.append(user_answers[z])
        polls.append(polls_for_final[i])

        polls = AllPollsSerializer(polls, many=True)
        answers = AllAnswersSerializer(answers, many=True)
        temp = {
            'poll': polls.data,
            'answers': answers.data
        }
        final.append(temp)

    print(final[0])

    return Response(final)


'''USER FUNCTIONAL'''
