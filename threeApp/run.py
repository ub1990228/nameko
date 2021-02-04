from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config['testing'])
from api import login_bp
app.register_blueprint(login_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run()
