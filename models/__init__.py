from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

entry_categories = db.Table(
    'entry_categories',
    db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)