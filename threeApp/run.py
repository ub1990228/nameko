from flask import Flask
from config import config
from flask_cors import *
from rpc import rpc

app = Flask(__name__)

CORS(app, supports_credentials=True)
app.config.from_object(config['testing'])
from api import login_bp
app.register_blueprint(login_bp, url_prefix='/api')
rpc.init_app(app)

if __name__ == '__main__':
    app.run()
