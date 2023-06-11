from sqlalchemy.exc import IntegrityError
from app.models import Question
from app import db


# Запись полученного вопросов в БД
def save_question(question) -> bool:
    new_record = Question(**question)
    try:
        db.session.add(new_record)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return False
    return True
