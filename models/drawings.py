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
        # check for people
        if not PeopleModel.find_person(recipient):
            raise Exception("Recipient does not exist")
        if not PeopleModel.find_person(sender):
            raise Exception("Sender does not exist")

        new_id = self.hash_drawing(drawing)
        # make sure no duplicate
        if not DrawingModel.find_by_id(new_id):
            self.id = new_id
            self.drawing = drawing
            self.date_time = datetime.now(tz=pytz.utc)
            self.recipient = recipient
            self.sender = sender
        else:
            raise Exception("ID already exists {}".format(new_id))

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
    def hash_drawing(cls, drawing):
        short_hash = hashlib.sha1(drawing.encode('utf-8')).hexdigest()[:10]
        # print(short_hash)
        id = int(short_hash, 16)
        # print(id)
        return id

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_drawing(cls, drawing):
        # return cls.query.filter_by(id=id).first()
        cls.find_by_id(cls.hash_drawing(drawing))
