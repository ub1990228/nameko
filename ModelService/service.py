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
                obj_model = self.model['obj']
                obj_model.insert_one(data)
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
        try:
            data = []
            stl_model = self.model['stl']
            if stl_model != None:
                for m in stl_model.find():
                    data.append(m['name'])
            obj_model = self.model['obj']
            if obj_model != None:
                for m in obj_model.find():
                    data.append(m['name'])
            
            return {'code':1,'data':data}
        except Exception as e:
            return {'code':0,'data':str(e)}

    @rpc
    def delete(self, data, type):
        try:
            if type == 'stl':
                stl_model = self.model['stl']
                stl_model.delete_one(data)
                return {'code': 1}
            elif type == 'obj':
                obj_model = self.model['obj']
                obj_model.delete_one(data)
                return {'code': 1}
            else:
                return {'code': 0}
        except:
            return {'code': 0}
            