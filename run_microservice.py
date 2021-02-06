# nameko run UserService.service --broker amqp://guest:guest@192.168.2.215
import eventlet 
eventlet.monkey_patch() # 使用ServiceRunner启动需要显示增加，不知道为什么
import importlib
from pathlib import Path
from UserService.service import UserService

root = Path(__file__).parent

def run_all():
    '''
    启动所有服务
    '''
    try:
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

        runner.start()
        runner.wait()
        # runner.stop()
    except Exception as e:
        runner.kill()

if __name__ == '__main__':
    run_all()
