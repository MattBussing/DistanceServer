from datetime import datetime

import pytz

from db import db
from models.people import PeopleModel


"""    string = '''
# {'matrix': "[['rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)
', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255,
255, 255)', 'rgb(255, 255, 255)'], ['rgb(255, 255, 255)', 'rgb(255, 255, 255)
', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255
, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)'], ['rgb(255, 255,
255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255,
255, 255)'], ['rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255,
255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(255, 255, 255)'], ['rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(18, 52, 86)', 'rgb(255, 255, 255)',
'rgb(18, 52, 86)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)'], ['rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)'],
['rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(255, 255, 255)'], ['rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)', 'rgb(255, 255, 255)', 'rgb(255, 255, 255)',
'rgb(255, 255, 255)']]", 'recipient': 'met'}
# '''
# 1500 is the len(string)
"""


class DrawingModel(db.Model):
    __tablename__ = 'drawings'
    id = db.Column(db.Integer, primary_key=True)
    drawing = db.Column(db.String(1500))
    date_time = db.Column(db.DateTime)
    recipient = db.Column(db.String(40),
                          db.ForeignKey('people.person')
                          )
    sender = db.Column(db.String(40),
                       db.ForeignKey('people.person')
                       )

    # def __init__(self, recipient, message):
    #     if PeopleModel.find_person(recipient):
    #         self.recipient = recipient
    #         self.message = message
    #         self.date_time = datetime.now(tz=pytz.utc)
    #     else:
    #         raise Exception("Person does not exist")
    #
    # def json(self):
    #     return {
    #         'recipient': self.recipient,
    #         'message': self.message,
    #         'dateTime': self.date_time.isoformat()
    #     }
    #
    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()
    #
    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()
    #
    # @classmethod
    # def search_for_message(cls, message, recipient):
    #     return cls.query.filter_by(message=message,
    #                                recipient=recipient).first()
    #
    # @classmethod
    # def find_all_by_recipient(cls, recipient):
    #     return cls.query.filter_by(recipient=recipient).all()
    #
    # @classmethod
    # def find_all(cls):
    #     return cls.query.order_by(cls.recipient).all()
