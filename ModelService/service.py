from nameko.rpc import rpc
from .dbhelper import DBHelper
from utils.dependencies import LoggingDependency

class ModelService:
    name = 'model_service'
    log = LoggingDependency()

    def __init__(self):
        self.dbhelper = DBHelper()
        self.model = self.dbhelper.db
    
    @rpc
    def save(self, data, type):
        try:
            if type == 'stl':
                stl_model = self.model['stl']
                stl_model.insert_one(data)
                return {'code': 1}
            elif type == 'obj':
                stl_model = self.model['obj']
                stl_model.insert_one(data)
                return {'code': 1}
            else:
                return {'code': 0}
        except:
            return {'code': 0}

    @rpc
    def read(self, name):
        pass
    
    @rpc
    def reads(self):
        pass
