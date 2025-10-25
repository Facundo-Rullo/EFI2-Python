from models import db
from models.entry import Entry

class EntryRepository:
    @staticmethod
    def get_all_published():
        return Entry.query.filter_by(is_published=True).all()
