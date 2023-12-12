from app import db
from sqlalchemy.orm import relationship

import datetime


class Favourites(db.Model):
    __tablename__ = "favourites"

    # PrimaryKey
    id = db.Column(db.Integer, primary_key=True, index=True)

    # ForeignKey
    superhero_id = db.Column(db.Integer, db.ForeignKey('superheros.id'), nullable=False, index=True)

    last_updated = db.Column(db.TIMESTAMP, onupdate=datetime.datetime.utcnow, nullable=True)
    created_on = db.Column(db.TIMESTAMP, default=datetime.datetime.utcnow)

    # Relationship
    superhero = relationship("Superheros")

    def __repr__(self):
        return f'<Superhero {self.id} - {self.superhero_id}>'
