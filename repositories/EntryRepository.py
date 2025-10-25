from models import db
from models.entry import Entry

class EntryRepository:
    @staticmethod
    def create(entry: Entry) -> None:
        db.session.add(entry)
        
    @staticmethod
    def get_all_published():
        return Entry.query.filter_by(is_published=True).all()
