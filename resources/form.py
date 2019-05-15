from flask import redirect, url_for
from flask_restful import Resource, reqparse

from models.message import MessageModel
from models.people import PeopleModel


class MessageForm(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message',
                        type=str,
                        required=True,
                        help="Message field cannot be left blank!"
                        )
    parser.add_argument('recipient',
                        type=str,
                        required=True,
                        help="Recipient field cannot be left blank!"
                        )

    def post(self):
        data = self.parser.parse_args()
        # since put it will update regardless
        # TODO delete
        if MessageModel.search_for_message(**data):
            return {'message': "A message like this already exists."}, 400

        message = MessageModel(**data)
        try:
            message.save_to_db()
        except:
            return {"message": "An error occurred while saving the item to \
the database."}, 500
        return redirect(url_for("home"))


class UserForm(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user',
                        type=str,
                        required=True,
                        help="Recipient field cannot be left blank!"
                        )
    parser.add_argument('form_type',
                        type=str,
                        required=True,
                        help="Recipient field cannot be left blank!"
                        )

    def post(self):
        data = self.parser.parse_args()

        if data["form_type"] == "add":

            # since put it will update regardless
            # TODO delete
            if PeopleModel.find_person(data['user']):
                return {'message': "This user already exists"}, 400

            person = PeopleModel(data["user"])
            try:
                person.save_to_db()
            except:
                return {"message": "An error occurred while saving the item \
to the database."}, 500

            return redirect(url_for("home"))

        elif data["form_type"] == "del":
            person = PeopleModel.find_person(data['user'])
            if person:
                try:
                    person.delete_from_db()
                except:
                    return {"message": "An error occurred while saving the item \
    to the database."}, 500
            else:
                return {'message': "Doesn't exist."}, 400

            return redirect(url_for("home"))
