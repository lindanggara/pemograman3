from flask import Flask
from board import pages   # import blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)  # daftar blueprint ke app
    return app

