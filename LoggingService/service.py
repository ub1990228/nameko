from nameko.rpc import rpc
from LoggingService.dbhelper import DBHelper

'''
登录服务
'''
class LoggingService:
    name = 'logging_service'

    def __init__(self):
        self.dbhelper = DBHelper()
        self.log = self.dbhelper.db.log
    
    @rpc
    def add_logging(self, log):
        try:
            pass
        except:
            pass
