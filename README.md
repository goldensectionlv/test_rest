Задача: спроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

Использовать следующие технологии: Django 2.2.10, Django REST framework.

# Инструкция
Перейдите на сайт приложения https://djang123.herokuapp.com/

Админка: https://djang123.herokuapp.com/admin

Логин и пароль: admin

# Документация по api

### 1. Создание опроса. 'POST'

https://djang123.herokuapp.com/api/create_poll

По данной ссылке передается Json-объект в формате:

    {
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
Как выглядит в админке: https://ibb.co/F73MXBW

    
2. Добавление вопроса к объекту опроса. 'POST'

https://djang123.herokuapp.com/api/add_question

По данной ссылке передается Json-объект в формате (указан id первого опроса в админке с именем 'Тестовый опрос 1'):

    {
    "poll_id": 5,
    "questions": "Добавленный вопрос",
    "question_type": "TEXT_ANSWER"
    }

3. Изменение вопроса. 'POST'

https://djang123.herokuapp.com/api/update_question

    {
    "poll_id": 5,
    "question_old": "Добавленный вопрос",
    "question_new": "Добавленный вопрос новый",
    "question_type": "TEXT_ANSWER"
    }
    
 4. Удаление одного вопроса. 'POST'
 
 https://djang123.herokuapp.com/api/delete_question
 
    {
    "poll_id": 4,
    "questions": "Тестовый вопрос"
    }
 
 5. Удаление всех вопросов у конкретного опроса 'POST'
 
 https://djang123.herokuapp.com/api/delete_all_questions
 
    {
    "poll_id": 2,
    "questions": "Тестовый вопрос"
    }
    
6. Оставить ответ на вопрос (текстовый). 'POST'

https://djang123.herokuapp.com/api/add_answer

    {
    "poll_id": 5,
    "question": "Тестовый вопрос",
    "answer": "Ответ",
    "question_type": "TEXT_ANSWER",
    "user_id": "123"
    }
user_id - передается произвольный. После запроса, если пользователя нет в базе данных, то он создается с этим айди. Если есть, то ответ привязывается к пользователю.

7. Выдача всех опросов. 'GET'

https://djang123.herokuapp.com/api/get_all_polls

Ответ выглядит так:
    
    [
    {
        "id": 4,
        "name": "Тестовый опрос 2",
        "date_starts": "2021-01-21",
        "date_ends": "2021-01-22",
        "description": "тут описание"
    },
    {
        "id": 6,
        "name": "Тестовый опрос 5",
        "date_starts": "2021-01-21",
        "date_ends": "2021-01-22",
        "description": "тут описание"
    },
    {
        "id": 5,
        "name": "Тестовый опрос 1",
        "date_starts": "2021-01-21",
        "date_ends": "2021-01-22",
        "description": "тут описание"
    }
    ]

8. Персональная выдача опросов и ответов пользователя, который запрашивает. 

https://djang123.herokuapp.com/api/get_user_polls/<int:user_id>

Пример:
https://djang123.herokuapp.com/api/get_user_polls/123


# К сожалению, это все, что успел. 
