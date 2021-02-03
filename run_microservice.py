from nameko.standalone.rpc import ClusterRpcProxy

CONFIG = {'AMQP_URI': "amqp://guest:guest@192.168.2.215"}

def compute():
    with ClusterRpcProxy(CONFIG) as rpc:
        rpc.user_service.login('admin')

if __name__ == '__main__':
    compute()
