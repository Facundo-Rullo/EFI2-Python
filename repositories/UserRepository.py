from models import db
from models.user import User

class UserRepository:
    @staticmethod
    def get_all_users_active():
        return User.query.filter_by(is_active=True).all()
    
    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.query.get_or_404(user_id)