from flask_restful import Resource, fields, marshal_with
from flask import request, abort
from rpc import rpc

class Models(Resource):
    templates = {
        'status': fields.Integer
    }

    def get(self):
        pass

    @marshal_with(templates)
    def post(self):
        template = dict()
        try:
            pass
        except Exception as e:
            print(e)
            template['status'] = 0
            return template
