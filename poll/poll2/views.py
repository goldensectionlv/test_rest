from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

# Create your views here.

'''Пример данных, отправляемых на бэкенд'''
example_create_poll = {
    "poll_name": "string",
    "date_starts": "2021-02-01",
    "date_ends": "2021-02-02",
    "description": "poll description text",
    "owner": 123
}
'''Конец примера'''


@api_view(['POST'])
def create_poll(request):
    if not request.user.is_superuser:
        return Response('Необходима авторизация в админке')

    poll_name = request.data['poll_name']
    date_starts = request.data['date_starts']
    date_ends = request.data['date_ends']
    description = request.data['description']
    owner = request.data['owner']

    try:
        custom_user = CustomUser.objects.get(id=owner)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if not Poll.objects.filter(name=poll_name).exists():
        poll_object = Poll.objects.create(
            name=poll_name,
            date_starts=date_starts,
            date_ends=date_ends,
            description=description,
            owner=custom_user
        )
        response = {"id": poll_object.id, "status": "Опрос создан"}
    else:
        response = f'Опрос с именем {poll_name} именем уже существует'

    return Response(response, status=status.HTTP_201_CREATED)


'''Пример данных, отправляемых на бэкенд'''
example_update_poll = {
    "poll_id": 8,
    "poll_name": "Updated",
    "date_ends": "2021-02-02",
    "description": "poll description text",
    "owner": 123
}
'''Пример данных, отправляемых на бэкенд'''


@api_view(['POST'])
def update_poll(request):
    if not request.user.is_superuser:
        return Response('Необходима авторизация в админке')

    poll_id = request.data["poll_id"]
    poll_name = request.data['poll_name']
    date_ends = request.data['date_ends']
    description = request.data['description']
    owner = request.data['owner']

    try:
        poll_object = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        response = f'Опрос с id {poll_id} не найден'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    try:
        user = CustomUser.objects.get(id=owner)
    except CustomUser.DoesNotExist:
        response = f'Пользователь с id {owner} не найден'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if Poll.objects.filter(name=poll_name).exists():
        return Response('Опрос с таким именем уже существует', status=status.HTTP_400_BAD_REQUEST)

    poll_object.name = poll_name
    poll_object.date_ends = date_ends
    poll_object.description = description
    poll_object.owner = user
    poll_object.save()

    return Response('Опрос изменен успешно', status=status.HTTP_202_ACCEPTED)


'''Айди для удаления передается через url'''


@api_view(['GET'])
def delete_poll(request, poll_id):
    if not request.user.is_superuser:
        return Response('Необходима авторизация в админке')

    try:
        poll_object = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        response = f'Опрос с id {poll_id} не найден'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    poll_object.delete()

    return Response(f'Опрос с id {poll_id} и именем {poll_object.name} удален')


'''Пример данных, отправляемых на бэкенд'''
example_add_question = {
    "poll_id": 8,
    "question_text": "Добавленный вопрос для опроса №2",
    "periodic_number": 2,
    "question_type": "TEXT_ANSWER"
}
'''Пример данных, отправляемых на бэкенд'''


@api_view(['POST'])
def add_question(request):
    if not request.user.is_superuser:
        return Response('Необходима авторизация в админке')

    poll_id = request.data["poll_id"]
    question_text = request.data["question_text"]
    question_type = request.data["question_type"]
    periodic_number = request.data["periodic_number"]

    try:
        poll_object = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    created_question = Question.objects.create(
        poll=poll_object,
        question_text=question_text,
        question_type=question_type,
        question_periodic_number=periodic_number
    )

    response = {"question_id": created_question.id,
                "status": "Вопрос создан"}

    return Response(response, status=status.HTTP_201_CREATED)


'''Пример данных, отправляемых на бэкенд'''
example_add_answer_option = {
    "poll_id": 8,
    "question_id": 13,
    "answer_option_name": "Опция раз"
}
'''Пример данных, отправляемых на бэкенд'''


@api_view(['POST'])
def add_answer_option(request):
    if not request.user.is_superuser:
        return Response('Необходима авторизация в админке')

    poll_id = request.data['poll_id']
    question_id = request.data['question_id']
    answer_option_name = request.data['answer_option_name']

    try:
        poll_object = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        response = f'Опрос с id {poll_id} не найден'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    try:
        question_object = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        response = f'Вопрос с id {question_id} не найден'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    answer_option_object = AnswerOption.objects.create(
        poll=poll_object,
        question=question_object,
        option_name=answer_option_name
    )

    response = {
        "answer_id": answer_option_object.id,
        "status": f"Вариант ответа для вопроса '{question_object.question_text}' создан"
    }

    return Response(response)


'''Пример данных, отправляемых на бэкенд'''
example_update_question = {
    "question_id": 6,
    "answer_option_id": 5,
    "question_text": "Измененный вопрос для опроса 8",
    "answer_type": "TEXT_ANSWER",
    "answer_option_name": "Вариант текстового ввода"
}
'''Пример данных, отправляемых на бэкенд'''


@api_view(['POST'])
def update_question(request):
    if not request.user.is_superuser:
        return Response('Необходима авторизация в админке')

    question_id = request.data["question_id"]
    answer_option_id = request.data["answer_option_id"]
    question_text = request.data["question_text"]
    answer_option_name = request.data["answer_option_name"]

    try:
        question_object = Question.objects.get(id=question_id)
        print('yes')
    except Question.DoesNotExist:
        response = f'Вопрос с id {question_id} не найден'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    try:
        answer_option_object = AnswerOption.objects.get(id=answer_option_id)
        print(answer_option_object.option_name)
    except Question.DoesNotExist:
        response = f'Вариант ответа (с id {answer_option_id}) на вопрос с id {question_id} не найден'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    question_object.question_text = question_text
    question_object.save()

    answer_option_object.option_name = answer_option_name
    answer_option_object.save()

    return Response('ok')


@api_view(['GET'])
def delete_question(request, question_id):
    if not request.user.is_superuser:
        return Response('Необходима авторизация в админке')

    try:
        question_object = Question.objects.get(id=question_id)
        question_object.delete()
    except Question.DoesNotExist:
        response = f'Вопроса с id {question_id} не найдено'
        return Response(response, status.HTTP_404_NOT_FOUND)

    return Response(f'Вопрос с id {question_id} удален', status=status.HTTP_200_OK)


@api_view(['GET'])
def get_poll(request, poll_id):
    try:
        poll_object = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        response = f'Опрос с id {poll_id} не найден'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    questions = poll_object.questions.all()

    poll_serializer = PollSerializer(poll_object, many=False)

    final_dict = []

    questions_with_answers = []

    for i in range(len(questions)):
        question_serializer = QuestionSerializer(questions[i], many=False)

        answers = AnswerOption.objects.filter(question=questions[i])

        answer_serializer = AnswerOptionSerializer(answers, many=True)

        questions_with_answers.append({
            questions[i].question_periodic_number: question_serializer.data,
            "answers": answer_serializer.data
        })

    final_dict.append({
        "poll": poll_serializer.data,
        "questions": questions_with_answers
    })

    return Response(final_dict)


@api_view(['GET'])
def get_all_polls(request):
    polls = Poll.objects.all()
    final_dict = []
    for i in range(len(polls)):

        poll_serializer = PollSerializer(polls[i], many=False)
        questions = Question.objects.filter(poll=polls[i])

        if len(questions) != 0:
            question_dict = []
            for z in range(len(questions)):
                question_serializer = QuestionSerializer(questions[z], many=False)

                answers = AnswerOption.objects.filter(question=questions[z]).all()

                answers_serializer = AnswerOptionSerializer(answers, many=True)

                question_dict.append({
                    questions[z].question_periodic_number: {
                        "question": question_serializer.data,
                        "answers": answers_serializer.data
                    }
                })
            final_dict.append({
                "poll": poll_serializer.data,
                "questions": question_dict
            })

    return Response(final_dict)


'''Пример данных, отправляемых на бэкенд'''
# example_add_answer = {
#     "user_id": 123,
#     "poll_id": 10,
#     "question_id": 13,
#     "answer_option_id": 13,
#     "text_answer": "это ответ для текстового поля",
#     "question_type": "OPTIONS_ANSWER",
#     "answer_boolean": true
# }
'''Пример данных, отправляемых на бэкенд'''


@api_view(['POST'])
def add_answer(request):
    user_id = request.data['user_id']
    poll_id = request.data['poll_id']
    question_id = request.data['question_id']
    answer_option_id = request.data['answer_option_id']
    question_type = request.data['question_type']

    try:
        poll_object = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        response = f'Ошибка в id опроса'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    try:
        question_object = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        response = f'Ошибка в id вопроса'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    try:
        answer_option_object = AnswerOption.objects.get(id=answer_option_id)
    except AnswerOption.DoesNotExist:
        response = f'Ошибка в id варианта'
        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if poll_object.id != question_object.poll.id or poll_object.id != answer_option_object.poll.id:
        return Response('Айди вопроса или ответа не относятся к выбранному опросу')

    try:
        if user_id != 0:
            user_object = CustomUser.objects.get(id=user_id)
        else:
            user_object = 0
    except CustomUser.DoesNotExist:
        return Response('Пользователь с таким id не найден')

    if question_type == 'TEXT_ANSWER':
        text_answer = request.data['text_answer']
        if user_id == 0:
            user_answer = UserAnswer.objects.create(
                question=question_object,
                answer_option=answer_option_object,
                poll=poll_object,
                text_answer=text_answer
            )
        else:
            print(question_object.poll.id, answer_option_object.poll.id, poll_object.id)
            user_answer = UserAnswer.objects.create(
                question=question_object,
                answer_option=answer_option_object,
                poll=poll_object,
                text_answer=text_answer,
                custom_user=user_object
            )
        serializer = UserAnswerSerializer(user_answer, many=False)
        return Response(serializer.data)

    elif question_type == 'OPTIONS_ANSWER':
        if user_id == 0:
            answer_boolean = request.data['answer_boolean']
            user_answer = UserAnswer.objects.create(
                question=question_object,
                answer_option=answer_option_object,
                poll=poll_object,
                answer_boolean=answer_boolean
            )
        else:
            answer_boolean = request.data['answer_boolean']
            user_answer = UserAnswer.objects.create(
                question=question_object,
                answer_option=answer_option_object,
                poll=poll_object,
                answer_boolean=answer_boolean,
                custom_user=user_object
            )
        serializer = UserAnswerSerializer(user_answer, many=False)
        return Response(serializer.data)


@api_view(['GET'])
def get_user_polls(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response(f'Пользователя с id {user_id} не найдено')

    user_answers = UserAnswer.objects.filter(custom_user=user)

    poll_list = []

    for i in range(len(user_answers)):
        if user_answers[i].poll.id not in poll_list:
            poll_list.append(user_answers[i].poll)

    final_dict = []
    for i in range(len(poll_list)):
        poll = poll_list[i]
        answers = []
        poll_serializer = PollSerializer(poll, many=False)
        for z in range(len(user_answers)):
            if user_answers[z].poll.id == poll_list[i].id:
                answers.append(user_answers[z])

        answers_serializer = UserAnswerSerializer(answers, many=True)
        final_dict.append({
            'poll': poll_serializer.data,
            'answers': answers_serializer.data
        })


    return Response(final_dict)
