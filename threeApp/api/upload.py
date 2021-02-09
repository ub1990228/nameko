import os,time
from flask_restful import Resource, fields, marshal_with, reqparse
from flask import request, abort
from rpc import rpc


class Upload(Resource):
    templates = {
        'status': fields.Integer,
        'path': fields.String
    }

    @marshal_with(templates)
    def post(self):
        template = dict()
        try:
            save_path = os.path.abspath(f'{__file__}/../../static/model')
            model_file = request.files.get('File')
            now_time = str(int(time.time()))
            model_name = f'{now_time}_{model_file.filename}'
            model_file.save(os.path.join(save_path, model_name))
            if os.path.exists(os.path.join(save_path, model_name)):
                model_path = f'/static/model/{model_name}'
            data = {
                'name': model_name,
                'path': model_path
            }
            if os.path.splitext(model_name)[-1][1:] == 'stl':
                res = rpc.model_service.save(data=data, type='stl')
            elif os.path.splitext(model_name)[-1][1:] == 'obj':
                res = rpc.model_service.save(data=data, type='obj')
            if res['code'] == 1:
                template['status'] = 1
                template['path'] = model_path
                return template
            else:
                if os.path.exists(os.path.join(save_path, model_name)):
                    os.remove(os.path.join(save_path, model_name))
                template['status'] = 0
                template['path'] = ''
                return template
        except Exception as e:
            print(e)
            template['status'] = 0
            template['path'] = ''
            return template
