import os
from app.models import User, Recording
from app import db
from app.tools import generate_uuid, convert_to_mp3
from app.config import records_dir


# Запись пользователя в БД, возвращает автоинкрементный ID
def user_save(username: str, uuid: str) -> int:
    user = User(username=username, uuid=uuid)
    db.session.add(user)
    db.session.commit()
    return user.id


# Проверка UUID токена пользователя
def user_check_uuid(user_id: int, user_uuid: str) -> bool:
    user = User.by_id(user_id)
    if user:
        return user.uuid == user_uuid
    return False


# Запись аудио в базу данных, в случае успешной конвертации и сохранения возвращает id записи
def recording_save(user_id: int, file) -> str:
    recording_uuid = generate_uuid()
    recording = Recording(user_id=user_id, uuid=recording_uuid)
    if convert_to_mp3(file, records_dir, recording.filename):
        db.session.add(recording)
        db.session.commit()
        return recording.id


# Получение пути к файлу .mp3 по id пользователя и записи
def recording_get_filename(user_id: int, recording_id: int) -> str:
    recording = Recording.by_id(recording_id)
    if recording and recording.user_id == user_id:
        return os.path.join('..', records_dir, recording.filename)
