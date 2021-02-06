from nameko.rpc import rpc
from .dbhelper import DBHelper
from utils.dependencies import LoggingDependency

'''
用户服务
'''
class UserService:
    name = 'user_service'
    log = LoggingDependency()

    def __init__(self):
        self.dbhelper = DBHelper()
        self.user = self.dbhelper.db
    
    @rpc
    def query(self, name, password):
        try:
            admin = self.user['admin']
            result = admin.find_one()
            if name == result['name'] and password == result['password']:
                return {'code': 1}
            else:
                return {'code': 0}
        except:
            return {'code': 0}
