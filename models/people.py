from db import db


class PeopleModel(db.Model):
    __tablename__ = 'people'
    person = db.Column(db.String(40), primary_key=True)
    messages = db.relationship("MessageModel")

    def __init__(self, person):
        self.person = person

    def json(self):
        return {
            'person': self.person,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        for m in self.messages:
            m.delete_from_db()

        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_person(cls, user):
        return cls.query.filter_by(person=user).first()
