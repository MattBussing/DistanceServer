from datetime import datetime

import pytz

from db import db

# from sqlalchemy import ForeignKey


class MessageModel(db.Model):
    __tablename__ = 'messages'

    recipient = db.Column(db.String(40),
                          db.ForeignKey('people.person'),
                          primary_key=True
                          )
    message = db.Column(db.String(240), primary_key=True)
    date_time = db.Column(db.DateTime)

    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message
        self.date_time = datetime.now(tz=pytz.utc)

    def json(self):
        return {
            'recipient': self.recipient,
            'message': self.message,
            'dateTime': self.date_time.isoformat()
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_for_message(cls, message, recipient):
        return cls.query.filter_by(message=message,
                                   recipient=recipient).first()

    @classmethod
    def find_all_by_recipient(cls, recipient):
        return cls.query.filter_by(recipient=recipient).all()

    @classmethod
    def find_all(cls):
        return cls.query.order_by(cls.recipient).all()
