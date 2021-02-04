# from nameko.standalone.rpc import ClusterRpcProxy

# CONFIG = {'AMQP_URI': "amqp://guest:guest@192.168.2.215"}

# def compute():
#     with ClusterRpcProxy(CONFIG) as rpc:
#         rpc.user_service.login('admin')

# if __name__ == '__main__':
#     compute()


# nameko run UserService/service --broker amqp://guest:guest@192.168.2.215
import importlib
from pathlib import Path

root = Path(__file__).parent


def run_all():
    services = {}
    for f in root.iterdir():
        if f.is_dir() and f.name.endswith('Service'):
            name = f.name
            service = importlib.import_module(name + '.service')
            services[name] = service
    from nameko.runners import ServiceRunner

    runner = ServiceRunner(config={'AMQP_URI': 'amqp://guest:guest@192.168.2.215'})
    for name, service in services.items():
        cls = getattr(service, name)
        runner.add_service(cls)

    print('start')
    runner.start()
    # runner.stop()


if __name__ == '__main__':
    run_all()