import requests


def get_questions(number: int = 1) -> list:
    url = 'https://jservice.io/api/random'
    params = {'count': number}
    headers = {'Accept': 'application/json'}
    req_answer = requests.get(url=url, params=params, headers=headers)
    if req_answer.status_code == 200:
        return req_answer.json()


