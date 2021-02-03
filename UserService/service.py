from nameko.rpc import rpc
# from UserService.dbhelper import DBHelper

'''
用户服务
'''
class UserService:
    name = 'user_service'

    def __init__(self):
        # self.dbhelper = DBHelper()
        # self.user = self.dbhelper.db.user
        print('start')
    
    @rpc
    def login(self, name):
        '''
        登录
        '''
        try:
            # result = self.user.find_one()
            # return {"code": 0, "msg": "", 'data': result}
            print(f'register{name}')
        except:
            pass
