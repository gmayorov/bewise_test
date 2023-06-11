from app import db


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String())
    answer = db.Column(db.String())
    created_at = db.Column(db.DateTime())

