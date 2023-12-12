from app import db
from sqlalchemy.orm import relationship

import datetime


class Superheros(db.Model):
    __tablename__ = "superheros"

    # PrimaryKey
    id = db.Column(db.Integer, primary_key=True, index=True)

    name = db.Column(db.String(255), nullable=False)

    last_updated = db.Column(db.TIMESTAMP, onupdate=datetime.datetime.utcnow, nullable=True)
    created_on = db.Column(db.TIMESTAMP, default=datetime.datetime.utcnow)

    # Relationship
    # organisation = favourites("Favourites")

    def __repr__(self):
        return f'<Superhero {self.id} - {self.name}>'
