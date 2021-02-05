from flask_restful import Resource, fields, marshal_with
from flask import request, abort

class Login(Resource):
    templates = {
        'status': fields.Integer
    }

    @marshal_with(templates)
    def get(self):
        try:
            template = dict()
            result = request.args
            if result.get('name') == 'admin' and result.get('password') == '123456':
                template['status'] = 1
                return template
            else:
                template['status'] = 0
                return template
        except:
            template['status'] = 0
            return template
