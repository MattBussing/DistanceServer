from flask_restful import Resource, reqparse
from resources.message import MessageModel


class Client(Resource):
    def get(self, _to):
        messages = MessageModel.find_all(_to)
    if messages:
        all = { 'messages' : [ m.json() for m in messages ] }
    else:
        all = { 'messages' : [ 'none' ]

    return all , 200
