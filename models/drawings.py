import hashlib
import json
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
    hash_value = db.Column(db.String(50))
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

        hashed_string = self.hash_drawing(drawing)
        # make sure no duplicate
        # if not DrawingModel.find_by_hash(hashed_string):
        self.drawing = drawing
        self.date_time = datetime.now(tz=pytz.utc)
        self.hash_value = hashed_string
        self.recipient = recipient
        self.sender = sender
        # else:
        #     raise Exception(
        #         "Duplicate already exists {}".format(hashed_string))

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

    def get_actual_vals(self):
        return json.loads(self.drawing)

    @classmethod
    def hash_drawing(cls, drawing):
        hash = str(hashlib.sha1(drawing.encode('utf-8')).hexdigest())
        # print(hash)
        return hash

    @classmethod
    def find_by_hash(cls, hash):
        return cls.query.filter_by(hash_value=hash).first()

    @classmethod
    def find_by_dsr(cls, drawing, sender, recipient):
        return cls.query.filter_by(hash_value=cls.hash_drawing(drawing),
                                   sender=sender,
                                   recipient=recipient).first()
        # return cls.find_by_hash(cls.hash_drawing(drawing, sender, recipient))

    @classmethod
    def find_all(cls):
        return cls.query.all()
