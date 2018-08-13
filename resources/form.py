from flask_restful import Resource, reqparse
from flask import render_template, make_response
from models.message import MessageModel


class Form(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
    )
    parser.add_argument('_to',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
    )

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('form.html'), 200, headers)

    def post(self):
        data = self.parser.parse_args()
        if MessageModel.search_for_message(**data):
            return {'message': "A message like this already exists."}, 400

        message = MessageModel(**data)
        try:
            message.save_to_db()
        except:
            return {"message": "An error occurred while saving the item to the database."}, 500

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('posted.html'), 200, headers)
