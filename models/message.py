from db import db
from datetime import datetime

class MessageModel(db.Model):
    __tablename__='messages'

    _to = db.Column(db.String(40), primary_key=True)
    message = db.Column(db.String(240), primary_key=True)
    dateTime = db.Column(db.DateTime)

    def __init__(self, _to, message):
        self._to = _to
        self.message = message
        self.dateTime = datetime.now()

    def json(self):
        return {
            'to': self._to,
            'message': self.message,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_for_message(cls, message, _to):
        return cls.query.filter_by(message=message, _to=_to).first()

    @classmethod
    def find_all(cls, _to):
        return cls.query.filter_by(_to=_to).all()
