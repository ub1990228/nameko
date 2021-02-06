from flask_restful import Api
from flask import Blueprint 
from api.login import Login
from api.models import Models

login_bp = Blueprint('login', __name__, url_prefix='/login')
api_login = Api(login_bp)
api_login.add_resource(Login, '/login/')
models_bp = Blueprint('models', __name__, url_prefix='/models')
api_models = Api(models_bp)
api_models.add_resource(Models, '/models/')
