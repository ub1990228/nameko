from flask_restful import Resource, fields, marshal_with
from flask import request, abort
from rpc import rpc

class Models(Resource):
    def get(self):
        pass
