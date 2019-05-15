from db import db


class PeopleModel(db.Model):
    __tablename__ = 'people'
    person = db.Column(db.String(40), primary_key=True)

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
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()
