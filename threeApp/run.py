from flask import Flask
from config import config
from flask_cors import *
from rpc import rpc

app = Flask(__name__)

CORS(app, supports_credentials=True)
app.config.from_object(config['testing'])

from api import login_bp
app.register_blueprint(login_bp, url_prefix='/api')
from api import upload_bp
app.register_blueprint(upload_bp, url_prefix='/api')
from api import models_bp
app.register_blueprint(models_bp, url_prefix='/api')
rpc.init_app(app)

if __name__ == '__main__':
    app.run(port='18888', debug=True, host='0.0.0.0')
