from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    @app.before_first_request
    def init_database():
        db.create_all()

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


