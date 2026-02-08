from flask import Flask
from flask_cors import CORS

from .apis import api


def create_app():
    app = Flask(__name__)
    CORS(app)
    api.init_app(app)
    return app
