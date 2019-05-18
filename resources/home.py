from flask import make_response, render_template
from flask_restful import Resource

from models.drawings import DrawingModel
from models.message import MessageModel
from models.people import PeopleModel


class Home(Resource):

    def get(self):
        people = PeopleModel.find_all()
        people = [person.person for person in people]

        messages = MessageModel.find_all()
        headers = {'Content-Type': 'text/html'}
        matrices = DrawingModel.find_all()
        for i in matrices:
            print(i.json())
        return make_response(render_template('home.html',
                                             people=people,
                                             messages=messages,
                                             title="DistancePi",
                                             matrices=DrawingModel.find_all()
                                             ),
                             200,
                             headers
                             )
