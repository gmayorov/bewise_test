from app import db


# Вспомогательный класс для поиска нужной записи в таблице по полю id
class Mixed:
    @classmethod
    def by_id(cls, uid):
        return db.session.query(cls).filter(cls.id == uid).first()


# Таблица для хранения пользователей
class User(db.Model, Mixed):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String())
    username = db.Column(db.String())
    recordings = db.orm.relationship("Recording", back_populates="user")


# Аудиозаписи. Связывается с таблицей пользователей соотношением "много к одному". Имя файла записи формируется из UUID
class Recording(db.Model, Mixed):
    __tablename__ = 'recordings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    uuid = db.Column(db.String())
    user = db.orm.relationship("User", back_populates="recordings", uselist=False)

    @property
    def filename(self):
        return self.uuid + '.mp3'


