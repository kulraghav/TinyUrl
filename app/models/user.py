from app import db
import datetime


class User(db.Model):
    """
    Model for users table
    """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
