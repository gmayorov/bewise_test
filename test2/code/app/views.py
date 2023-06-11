from flask import request, send_file
from flask_restful import Resource

from app import app_port
from app.storage import user_save, user_check_uuid, recording_save, recording_get_filename
from app.tools import generate_uuid


class User(Resource):

    # Создание нового пользователя
    def post(self):
        username = request.json['username']
        if not username:
            return {'error': 'Invalid username'}, 400
        user_uuid = generate_uuid()
        user_id = user_save(username, user_uuid)
        if user_id:
            return {'message': 'User appended', 'user_id': user_id, 'user_uuid': user_uuid}
        return {'error': 'User can\'t be appended'}, 500


class Record(Resource):

    # Проверка токена пользователя и сохранение аудио в случае успеха
    def post(self):
        user_id = request.values.get('user_id')
        user_uuid = request.values.get('user_uuid')
        if not user_check_uuid(user_id=user_id, user_uuid=user_uuid):
            return {'error': 'Not authorized'}, 401
        if 'audio' not in request.files:
            return {'message': 'No audio in the request'}, 400
        file = request.files['audio']
        recording_id = recording_save(user_id=user_id, file=file)
        if recording_id:
            url = f'http://localhost:{app_port}/record?id={recording_id}&user={user_id}'
            return {'message': 'File successfully uploaded', 'url': url}, 201

    # Скачивание сохраненного аудио при правильном указании id записи и пользователя в параметрах запроса
    def get(self):
        recording_id = int(request.args.get('id'))
        user_id = int(request.args.get('user'))
        filename = recording_get_filename(user_id=user_id, recording_id=recording_id)
        if filename:
            return send_file(filename, as_attachment=True)
        return {'error': 'File not found'}, 404
