from app import db
import datetime


class Url(db.Model):
    """
    Model for url table
    """

    __tablename__ = "urls"

    today = datetime.datetime.now()
    # Set the expiration for another 40 days
    expiration = today + datetime.timedelta(days=40)

    hash = db.Column(db.String(16), primary_key=True)
    original_url = db.Column(db.String(512), nullable=False)
    user_id = db.Column(db.Integer, index=True, nullable=True)
    creation_date = db.Column(db.DateTime, default=today)
    expiration_date = db.Column(db.DateTime, default=expiration)
