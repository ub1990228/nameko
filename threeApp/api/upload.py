import os,time
from flask_restful import Resource, fields, marshal_with, reqparse
from flask import request, abort


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
            template['status'] = 1
            template['path'] = f'/static/model/{model_name}'
            return template
        except Exception as e:
            template['status'] = 0
            template['path'] = ''
            return template
