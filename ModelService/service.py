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
                model_dict = data
                stl_model.insert_one(model_dict)
                return {'code': 1}
            elif type == 'obj':
                return {'code': 0}
            else:
                return {'code': 0}
        except:
            return {'code': 0}

    @rpc
    def read(self):
        pass
    
    @rpc
    def write(self):
        pass
