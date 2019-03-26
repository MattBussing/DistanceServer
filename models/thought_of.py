# Author Matt Bussing

from db import db


class ThoughtOfModel(db.Model):
    __tablename__ = 'thought_of'

    _to = db.Column(db.String(40), primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self, _to, increase_count_by):
        self._to = _to
        old_count = ThoughtOfModel.find_count(_to).count
        print(old_count)
        # this is so we can increment each one
        if old_count:
            self.count = old_count + increase_count_by
        else:
            self.count = increase_count_by

    def json(self):
        return {
            'to': self._to,
            'count': self.count
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_count(cls, _to):
        return cls.query.filter_by(_to=_to).first()

    # @classmethod
    # def find_all(cls, _to):
    #     return cls.query.filter_by(_to=_to).all()
