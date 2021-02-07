from flask_restful import Resource, fields, marshal_with
from flask import request, abort
from rpc import rpc

class Login(Resource):
    templates = {
        'status': fields.Integer
    }

    @marshal_with(templates)
    def get(self):
        template = dict()
        try:
            result = request.args
            
            res = rpc.user_service.query(
                name=result.get('name'), 
                password=result.get('password')
            )
            if res['code'] == 1:
                template['status'] = 1
                return template
            else:
                template['status'] = 0
                return template
        except Exception as e:
            print(e)
            template['status'] = 0
            return template
