import requests
from datetime import datetime


# Скачивание вопросов викторины. В случае неудачи возвращается None
def get_question() -> dict:
    url = 'https://jservice.io/api/random'
    params = {'count': 1}
    headers = {'Accept': 'application/json'}
    req_answer = requests.get(url=url, params=params, headers=headers, timeout=1)
    if req_answer and req_answer.status_code == 200:
        question = req_answer.json()[0]
        str_created_at = question['created_at'].split('.')[0]
        created_at = datetime.strptime(str_created_at, "%Y-%m-%dT%H:%M:%S")
        return {'id': question['id'],
                'question': question['question'],
                'answer': question['answer'],
                'created_at': created_at}
