from flask_restful import Resource, reqparse
from models.message import MessageModel


class Client(Resource):
    def get(self, _to):
        messages = MessageModel.find_all(_to)
        all = []
        if messages:
            all = [ m.json() for m in messages ]
        else:
            all = [ 'none' ]

        return { 'messages' : all } , 200
