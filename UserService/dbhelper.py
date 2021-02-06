class DBHelper(object):
    # 单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(DBHelper, '_instance'):
            DBHelper._instance = object.__new__(DBHelper)
        return DBHelper._instance

    def __init__(self, conf=None):
        if not conf:
            from settings import DATABASE as conf
        uri = 'mongodb://%s:%s@%s:%s' % (conf['user'], conf['password'], conf['host'], conf['port'])
        from pymongo import MongoClient
        self.client = MongoClient(uri)
        self.db = self.client[conf['database']]

    def close(self):
        self.client.close()
