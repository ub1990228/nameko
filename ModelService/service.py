from nameko.rpc import rpc
from .dbhelper import DBHelper
from utils.dependencies import LoggingDependency

class ModelService:
    name = 'model_service'
    log = LoggingDependency()

    def __init__(self):
        pass
    
    @rpc
    def save(self):
        pass
