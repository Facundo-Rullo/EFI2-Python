from models import db
from models.user import User

class UserRepository:
    
    @staticmethod
    def get_by_id(user_id: int) -> User:
        return User.query.get_or_404(user_id)