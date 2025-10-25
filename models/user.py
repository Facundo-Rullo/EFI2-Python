from . import db  # Importamos 'db' desde el __init__.py
from datetime import datetime
class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    entries = db.relationship('Entry', backref='autor_entries', lazy=True)
    comments = db.relationship('Comment', backref='autor_comments', lazy=True)

    def __str__(self):
        return self.username
    