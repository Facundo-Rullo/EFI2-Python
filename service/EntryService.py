from repositories.EntryRepository import EntryRepository

class EntryService:
    def __init__(self):
        self.repo = EntryRepository()
    
    def get_public_posts(self):
        return self.repo.get_all_published()
