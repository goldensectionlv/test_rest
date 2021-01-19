from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import *
from .models import *


# упрощенная версия авторизации
def get_user_id_or_create(user_id):
    try:
        user_data = UserPoll.objects.get(id=user_id)
    except:
        UserPoll.objects.get_or_create(id=user_id)
        user_data = UserPoll.objects.get(id=user_id)
    return user_data


'''CRUD'''

a = {
    "poll": {
        "name": "Тестовый опрос 1",
        "date_starts": "2021-01-21",
        "date_ends": "2021-01-22",
        "description": "тут описание"
    },
    "questions": {
        "question_text": "Тестовый вопрос",
        "question_type": "TEXT_ANSWER"
    }
}


# Создание опроса с изначальными вопросами
@api_view(['POST'])
def create_poll(request):
    response = []
    if request.user.is_superuser:
        poll_object = None
        question_object = None
        poll_serializer = PollSerializer(data=request.data['poll'])

        print(request.user.is_superuser)

        if poll_serializer.is_valid():
            # сохраняю тут и таким образом для того, чтобы получить автоматически сгенерированный id
            poll_object = Poll.objects.create(**poll_serializer.validated_data)
            poll_object.save()
            response.append({
                'poll_creation': True,
                'poll_data': poll_serializer.data
            })
        else:
            print('poll no')

        question_serializer = QuestionSerializer(data=request.data['questions'])
        if question_serializer.is_valid():
            question_object = Question.objects.create(**question_serializer.validated_data, poll=poll_object)
            question_object.save()

            response.append({
                'poll_questions': question_serializer.data
            })
    else:
        response = 'Ошибка авторизации. Для публикации вопроса войдите в панель администратора'
    return Response(response)


# Добавление вопроса
@api_view(['POST'])
def add_question(request):
    response = ''
    if request.user.is_superuser:
        poll_id = request.data['poll_id']
        question = request.data['questions']
        question_type = request.data['question_type']

        if not Question.objects.filter(poll_id=poll_id, question_text=question).exists():
            Question.objects.create(poll_id=poll_id, question_text=question, question_type=question_type)
            response = f'Вопрос "{question}" добавлен к опросу с id {poll_id}'
        else:
            response = f'Вопрос "{question}" уже существует или неправильный id опроса'
    else:
        response = 'Ошибка авторизации. Для публикации вопроса войдите в панель администратора'
    return Response(response)


#  Изменение данных вопроса
@api_view(['POST'])
def update_question(request):
    response = ''
    if request.user.is_superuser:
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
            response = QuestionSerializer(question_object, many=False)
        else:
            response = 'Вопрос отсутствует в базе данных или неправильный id опроса'
    else:
        response = 'Ошибка авторизации. Для публикации вопроса войдите в панель администратора'

    return Response(response)


# Удаление конкретного вопроса

@api_view(['POST'])
def delete_question(request):
    response = ''
    if request.user.is_superuser:
        poll_id = request.data['poll_id']
        question = request.data['questions']

        if Question.objects.filter(poll_id=poll_id, question_text=question).exists():
            Question.objects.get(poll_id=poll_id, question_text=question).delete()
            response = f'Вопрос "{question}" удален'
        else:
            response = f'Вопрос "{question}" отсутствует в базе данных'
    else:
        response = 'Ошибка авторизации. Для публикации вопроса войдите в панель администратора'

    return Response(response)


# Удаление всех вопросов

@api_view(['POST'])
def delete_all_questions(request):
    response = ''
    if request.user.is_superuser:
        poll_id = request.data['poll_id']
        question = Question.objects.filter(poll_id=poll_id)

        # Проверка на наличие вопросов
        if len(question) > 0:
            for i in range(len(question)):
                question[i].delete()
            response = 'Все вопросы удалены'
        else:
            response = 'Список вопросов пуст'
    else:
        response = 'Ошибка авторизации. Для публикации вопроса войдите в панель администратора'

    return Response(response)


'''CRUD END'''

'''USER FUNCTIONAL'''


# {
# "poll_id": 122,
# "question": "Тестовый вопрос",
# "answer": "Ответ",
# "question_type": "TEXT_ANSWER",
# "user_id": 0
# }
@api_view(['POST'])
def add_answer(request):
    poll_id = request.data['poll_id']
    question = request.data['question']
    answer = request.data['answer']
    # question_type = request.data['question_type']
    user_id = request.data['user_id']

    is_question_exist = Question.objects.filter(poll_id=poll_id, question_text=question).exists()
    if is_question_exist:
        question_object = Question.objects.get(poll_id=poll_id, question_text=question)
    else:
        return Response(f'Ошибка, вероятно вопрос "{question}" не существует')

    # Если у юзера есть id. 0 - дефолтное значение, говорящее об отсутствии id
    if user_id != 0:
        user_data = get_user_id_or_create(user_id=user_id)
        Answer.objects.create(question=question_object, answer_with_text=answer, user_poll=user_data,
                              poll_id=poll_id)
        response = f'Ответ к вопросу "{question_object.question_text}" добавлен от пользователя c id {user_data.id}'

    else:
        Answer.objects.create(question=question_object, answer_with_text=answer,
                              poll_id=poll_id)
        response = f'Анонимный ответ к вопросу "{question_object.question_text}" добавлен'

    return Response(response)


@api_view(['GET'])
def get_all_polls(request):
    polls = Poll.objects.all()

    if len(polls) > 1:
        serializer = AllPollsSerializer(polls, many=True)
    else:
        serializer = AllPollsSerializer(polls)

    return Response(serializer.data)


@api_view(['GET'])
def get_user_polls(request, user_id):
    final = []
    if UserPoll.objects.filter(id=user_id).exists():
        user_answers = Answer.objects.filter(user_poll=user_id)

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
    else:
        final = f'Пользователя с id {user_id} не существует'

    return Response(final)


'''USER FUNCTIONAL'''
