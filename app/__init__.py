from flask import Flask
import os
from .routes import main

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, "..", "templates")
    static_dir = os.path.join(base_dir, "..", "static")

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    app.register_blueprint(main)

    return app