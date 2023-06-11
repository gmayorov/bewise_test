import os
from flask import request
from flask_restful import Resource
from app.source import get_question
from app.storage import save_question


class Do(Resource):

    # Скачивание вопросов викторины:
    # В задании указано, что в качестве ответа должен отправляться последний сохраненный вопрос викторины,
    # сохранить вопрос можно только получив, не сказано, надо ли завершать попытки его получения при неудаче,
    # поэтому попытки продолжаются, пока вопрос не будет получен. Но если запросить 0 вопросов вернется пустой ответ.
    # Либо я неправильно понял задание, извиняюсь.
    def post(self):
        questions_num = int(request.json['questions_num'])
        if questions_num < 0:
            return {'error': 'Nothing to fetch'}, 400
        saved = 0
        result = None
        while saved < questions_num:
            question = get_question()
            if not question:
                continue
            ok = save_question(question)
            if ok:
                result = question
                saved += 1
        if result:
            result.pop('created_at')
        return result, 200
