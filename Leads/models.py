from .extensions import db
from datetime import datetime

class Lead(db.Model):
    __tablename__ = "leads"

    id = db.Column(db.Integer, primary_key=True)

    # Personal Information
    full_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(30), nullable=False)

    # Location
    country = db.Column(db.String(100), nullable=False)

    # Product Information
    product = db.Column(db.String(120), nullable=False)

    # Marketing Data
    source = db.Column(db.String(100), default="Website")

    # Lead Status
    status = db.Column(
        db.String(50),
        default="New"
    )

    # Notes
    notes = db.Column(db.Text)

    # Date
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Lead {self.full_name}>"