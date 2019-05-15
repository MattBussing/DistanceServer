from flask import make_response, render_template
from flask_restful import Resource

# from jinja2 import Template
#
# from models.message import MessageModel
from models.people import PeopleModel


class Home(Resource):

    def get(self):
        people = PeopleModel.find_all()
        people = [person.person for person in people]
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html', people=people), 200,
                             headers)
