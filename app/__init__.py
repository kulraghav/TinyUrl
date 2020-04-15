from flask import Flask, request, jsonify
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

    @app.route('/api/v1/shorten_url', methods=['POST'])
    def shorten_url():
        original_url = request.form['original_url']

        return original_url

    return app


