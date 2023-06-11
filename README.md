# Тестовое задание BeWise.ai

## Подготовка и запуск

Склонировать репозиторий на локальную машину:

    git clone https://github.com/gmayorov/bewise_test.git
    cd bewise_test

По умолчанию порт API первого задания теста 65231, для второго 65232. В случае необходимости порты можно изменить в файле .env:

    TEST1_PORT=65231
    TEST2_PORT=65232

Можно запускать:

    docker-compose up

Через минуту запустится (я надеюсь) и можно приступать к проверке

## Проверка
Если изменили порты, надо будет поправить в соответствующих командах.
В соседной консоли можно выполнить следующие команды
### Первое задание:

    curl -X POST http://localhost:65231/do -H 'Content-Type: application/json' -d '{"questions_num":5}'

 Ответ, последний вопрос (без даты создания, но дата записывается в БД):

     {
        "id": 102361,
        "question": "...ace, another term for this golf feat",
        "answer": "a hole in one"
    }
### Второе задание:
создаем двух пользователей:

    curl -X POST http://localhost:65232/user -H 'Content-Type: application/json' -d '{"username":"user1"}'
    {"message": "User appended", "user_id": 1, "user_uuid": "токен 1"}
    
    curl -X POST http://localhost:65232/user -H 'Content-Type: application/json' -d '{"username":"user2"}'
    {"message": "User appended", "user_id": 2, "user_uuid": "токен 2"}

Отправляем аудиофайлы, два для первого пользователя и один для второго (вместо "токен 1" и "токен 2" подставить полученные на прошлом шаге токены):

    curl -X POST -F 'audio=@sample1.wav' -F 'user_id=1' -F 'токен 1' localhost:65232/record
    {"message": "File successfully uploaded", "url": "http://localhost:65232/record?id=1&user=1"}
    
    curl -X POST -F 'audio=@sample2.wav' -F 'user_id=1' -F 'токен 1' localhost:65232/record
    {"message": "File successfully uploaded", "url": "http://localhost:65232/record?id=2&user=1"}
    
    curl -X POST -F 'audio=@sample3.wav' -F 'user_id=2' -F 'токен 2' localhost:65232/record
    {"message": "File successfully uploaded", "url": "http://localhost:65232/record?id=3&user=2"}

Если открыть полученные ссылки в браузере, скачаются сконвертированные семплы.
