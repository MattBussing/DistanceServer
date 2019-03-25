# Author Matt Bussing

from db import db


class ThoughtOfModel(db.Model):
    __tablename__ = 'thought_of'

    _to = db.Column(db.String(40), primary_key=True)
    count = db.Column(db.Int)

    def __init__(self, _to, count):
        self._to = _to
        self.count = count

    def json(self):
        return {
            'to': self._to,
            'thought_of': self.message
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def search_for_count(cls, _to):
        return cls.query.filter_by(_to=_to).first()

    # @classmethod
    # def find_all(cls, _to):
    #     return cls.query.filter_by(_to=_to).all()
