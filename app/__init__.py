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

        # TODO:
        # Validate if original_url is a valid URL
        # If yes, generate a short URL
        # Otherwise, throw an error

        return original_url

    @app.route('/api/v1/get_url/<string:url>', methods=['GET'])
    def get_url(url):

        # TODO:
        # Check if the URL exist
        # If yes, redirect to original_url
        # Otherwise, throw an error

        return url


    return app


