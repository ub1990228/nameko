from flask_restful import Api
from flask import Blueprint 
from threeApp.api.login import Login


# 注册生成PDF报告蓝图
login_bp = Blueprint('login', __name__, url_prefix='/login')
api_login = Api(login_bp)
api_login.add_resource(Report, '/login/')
