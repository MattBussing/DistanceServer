import hashlib
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

    def __init__(self, drawing, recipient, sender):
        # print
        hash_object = hashlib.sha256(drawing)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
        # TODO finish , get recipient and sender
        if PeopleModel.find_person(recipient) \
                and PeopleModel.find_person(sender):
            self.id = hex_dig
            self.drawing = drawing
            self.date_time = datetime.now(tz=pytz.utc)
            self.recipient = recipient
            self.sender = sender
        else:
            raise Exception("Sender or Recipient does not exist")

    def json(self):
        return {
            'id': self.id,
            'drawing': self.drawing,
            'date_time': self.date_time.isoformat(),
            'recipient': self.recipient,
            'sender': self.sender
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_for_drawing_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
