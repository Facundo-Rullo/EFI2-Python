from models import db
from models.entry import Entry
from repositories.EntryRepository import EntryRepository

class EntryService:
    def __init__(self):
        self.repo = EntryRepository()
        
    def create_entry(self, data: dict, user_id: int) -> Entry:
        new_entry = Entry(
            title = data.get("title"),
            content = data.get("content"),
            user_id = user_id
        )

        try:
            self.repo.create(new_entry)
            db.session.commit()
            return new_entry
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error al crear el post: {str(e)}") 

    
    def get_public_posts(self):
        return self.repo.get_all_published()
