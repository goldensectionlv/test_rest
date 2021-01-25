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
# Инструкция v2
### Перейдите на сайт приложения https://djang123.herokuapp.com/

### Админка: https://djang123.herokuapp.com/admin

## Логин и пароль: admin

## Все необходимые модели в админке выведены и связаны.

# Документация по api








## Инструкция v1
### Перейдите на сайт приложения https://djang123.herokuapp.com/

### Админка: https://djang123.herokuapp.com/admin

## Логин и пароль: admin

## Все необходимые модели в админке выведены и связаны.

# Документация по api

### 1. Создание опроса.

#### Метод: POST

#### URL: https://djang123.herokuapp.com/api/create_poll

#### Права: доступно только при авторизации под админом через админку

Пока что поддерживается добавление только одного вопроса при создании опроса. Для добавления остальных, следует воспользоваться п.2.

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

    
### 2. Добавление вопроса к объекту опроса. 'POST'

#### Метод: POST

#### URL: https://djang123.herokuapp.com/api/add_question

#### Права: доступно только при авторизации под админом через админку

Существует три фиксированных значения для ключа "question_type". Можно выбрать один из них: 

#### "TEXT_ANSWER"
#### "ONE_OPTION_ANSWER"
#### "MANY_OPTIONS_ANSWER"


По данной ссылке передается Json-объект в формате:

    {
    "poll_id": 5,
    "questions": "Добавленный вопрос",
    "question_type": "TEXT_ANSWER"
    }

### 3. Изменение вопроса. 'POST'

#### Метод: POST

#### URL: https://djang123.herokuapp.com/api/update_question

#### Права: доступно только при авторизации под админом через админку

Пример передаваемых данных:

    {
    "poll_id": 5,
    "question_old": "Добавленный вопрос",
    "question_new": "Добавленный вопрос новый",
    "question_type": "TEXT_ANSWER"
    }
    
 ### 4. Удаление одного вопроса. 'POST'
 
 https://djang123.herokuapp.com/api/delete_question
 
    {
    "poll_id": 4,
    "questions": "Тестовый вопрос"
    }
 
 ### 5. Удаление всех вопросов у конкретного опроса 'POST'
 
 https://djang123.herokuapp.com/api/delete_all_questions
 
    {
    "poll_id": 2
    }
    
### 6. Оставить ответ на вопрос (текстовый). 'POST'

#### Метод: POST

#### URL: https://djang123.herokuapp.com/api/add_answer

#### Права: доступно всем

Анонимное использование: проставьте значение в ключе "user_id": 0
Создание пользователя в системе: проставьте произвольный числовой id (integer). Пример: "user_id": 666
Авторизация: передайте существующий id пользователя (model UserPoll)

Существует три фиксированных значения для ключа "question_type". Можно выбрать один из них: 

#### "TEXT_ANSWER"

При выборе этого варианта данные передаются в следующем формате:

    {
    "poll_id": 7,
    "question": "вопрос",
    "answer": true,
    "question_type": "TEXT_ANSWER",
    "user_id": 123
    }
    
#### "ONE_OPTION_ANSWER"

При выборе этого варианта данные передаются в следующем формате:

    {
    "poll_id": 7,
    "question": "вопрос тру фолс",
    "answer": true,
    "question_type": "ONE_OPTION_ANSWER",
    "user_id": 123
    }

#### "MANY_OPTIONS_ANSWER"

При выборе этого варианта данные передаются в следующем формате (все з:

    {
    "poll_id": 7,
    "question": "Тестовый вопрос",
    "question_type": "MANY_OPTIONS_ANSWER",
    "user_id": 123,
    "vote_one": true,
    "vote_two": null,
    "vote_three": true,
    "vote_one_desc": "description 1",
    "vote_two_desc": "description 2",
    "vote_three_desc": "description 3"
    }


### 7. Выдача всех опросов. 'GET'

#### Метод: GET

#### URL: https://djang123.herokuapp.com/api/get_all_polls

#### Права: доступно всем


Ответ выглядит так:

        {
        "poll": {
            "id": 115,
            "name": "Тестовый опрос 1",
            "date_starts": "2021-01-21",
            "date_ends": "2021-01-22",
            "description": "тут описание",
            "owner": null
        },
        "questions": [
            {
                "id": 52,
                "question_text": "Тестовый вопрос",
                "question_type": "TEXT_ANSWER",
                "poll": 115
            }
        ]
    },
    {
        "poll": {
            "id": 116,
            "name": "Тестовый опрос 1",
            "date_starts": "2021-01-21",
            "date_ends": "2021-01-22",
            "description": "тут описание",
            "owner": null
        },
        "questions": [
            {
                "id": 53,
                "question_text": "Тестовый вопрос",
                "question_type": "TEXT_ANSWER",
                "poll": 116
            }
        ]
    },
    
### 8. Запрос конкретного опроса по id.


#### Метод: GET

#### URL: https://djang123.herokuapp.com/api/get_poll/<int:poll_id>

#### Права: доступно всем

Пример ссылки: https://djang123.herokuapp.com/api/get_poll/5

Пример ответа: 

    {
    "poll": {
        "id": 126,
        "name": "Тестовый опрос 1",
        "date_starts": "2021-01-21",
        "date_ends": "2021-01-22",
        "description": "тут описание"
    },
    "questions": [
        {
            "id": 65,
            "question_text": "Тестовый вопрос",
            "question_type": "TEXT_ANSWER",
            "poll": 126
        }
    ]
    }
    
### 9. Запрос конкретного вопроса по его id.

#### Метод: GET

#### URL: https://djang123.herokuapp.com/api/get_question/<int:question_id>

#### Права: доступно всем

Пример: https://djang123.herokuapp.com/api/get_question/5

Пример ответа:

    {
    "id": 64,
    "question_text": "Добавленный вопрос",
    "question_type": "MANY_OPTIONS_ANSWER",
    "poll": 125
    }


### 10. Персональная выдача опросов и ответов пользователя, который запрашивает. 

#### Метод: GET

#### URL: https://djang123.herokuapp.com/api/get_user_polls/<int:user_id>

#### Права: доступно всем

Пример:
https://djang123.herokuapp.com/api/get_user_polls/123


