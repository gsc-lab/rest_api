from flask import Flask, jsonify
from flask_cors import CORS

from .apis import api


def create_app():
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024  # 1MB
    CORS(app)
    api.init_app(app)

    @app.errorhandler(Exception)
    def handle_exception(e):
        code = getattr(e, "code", 500)
        if not isinstance(code, int):
            code = 500
        if code == 500:
            return jsonify(message="internal server error"), 500
        return jsonify(message=str(e)), code

    return app
