from models import db
from models.user import User
from repositories.UserRepository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()
        
    def get_users_active(self):
        return self.repo.get_all_users_active()
    
    def get_user_by_id(self, user_id: int):
        return self.repo.get_user_by_id(user_id)