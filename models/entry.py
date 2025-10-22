from . import db, entry_categories # Importamos 'db' y la tabla de asociación
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entry'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    is_published = db.Column(db.Boolean, default=True)
    updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    comments = db.relationship('Comment', backref='entry_comments', lazy=True)
    categories = db.relationship(
        'Category', 
        secondary=entry_categories, # Usamos la tabla importada
        backref=db.backref('entry_categories', lazy=True)
    )

    def __str__(self):
        return self.title
