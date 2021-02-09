import os
from flask_restful import Resource, fields, marshal_with
from flask import request, abort
from rpc import rpc


class Models(Resource):
    templates = {
        'status': fields.Integer,
        'data': fields.List(fields.String)
    }

    @marshal_with(templates)
    def get(self):
        template = dict()
        try:
            res = rpc.model_service.reads()
            if res['code'] == 1:
                template['status'] = 1
                template['data'] = res['data']
                return template
            else:
                template['status'] = 0
                template['data'] = []
                return template
        except:
            template['status'] = 0
            template['data'] = []
            return template

    @marshal_with(templates)
    def post(self):
        template = dict()
        try:
            pass
        except Exception as e:
            print(e)
            template['status'] = 0
            template['data'] = []
            return template

    @marshal_with(templates)
    def delete(self):
        template = dict()
        try:
            save_path = os.path.abspath(f'{__file__}/../../static/model')
            result = request.args
            model_path = os.path.join(save_path, result.get('name'))
            data = {
                'name': result.get('name')
            }
            if os.path.splitext(result.get('name'))[-1][1:] == 'stl':
                res = rpc.model_service.delete(data=data, type='stl')
            elif os.path.splitext(result.get('name'))[-1][1:] == 'obj':
                res = rpc.model_service.delete(data=data, type='obj')
            if res['code'] == 1:
                if os.path.exists(model_path):
                    os.remove(model_path)
                template['status'] = 1
                template['data'] = []
                return template
            else:
                template['status'] = 0
                template['data'] = []
                return template
        except Exception as e:
            print(e)
            template['status'] = 0
            template['data'] = []
            return template
