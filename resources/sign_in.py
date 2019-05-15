from flask import make_response, render_template
from flask_restful import Resource, reqparse
from jinja2 import Template

from models.message import MessageModel
from models.people import PeopleModel


class SignIn(Resource):

    def get(self):

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('bootstrap/sign_in.html'), 200,
                             headers)
