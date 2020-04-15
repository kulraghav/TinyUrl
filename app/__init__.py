from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.models.user import User
    from app.models.url import Url

    @app.before_first_request
    def initialize_database():
        db.create_all()

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/api/v1/shorten_url', methods=['POST'])
    def shorten_url():
        """
        Method that will generate a tiny url
        :return:
        """
        original_url = request.form['original_url']

        # TODO:
        # Validate if original_url is a valid URL
        # If yes, generate a short URL
        # Otherwise, throw an error

        return original_url

    @app.route('/api/v1/get_url/<string:url>', methods=['GET'])
    def get_url(url):
        """
        Method that will redirect url
        :param url:
        :return:
        """
        # TODO:
        # Check if the URL exist
        # If yes, redirect to original_url
        # Otherwise, throw an error

        return url

    return app
