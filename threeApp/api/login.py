from flask_restful import Resource, fields, marshal_with
from flask import request, abort

class Login(Resource):
    templates = {
        'status': fields.Integer
    }

    @marshal_with(templates)
    def get(self):
        try:
            template = {}
            result = request.get_json()
            if result['name'] == 'admin' and result['password'] == '123456':
                return template['status'] = 1
            else:
                return template['status'] = 0
        except:
            return template['status'] = 0
