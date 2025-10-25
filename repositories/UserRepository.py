from models import db
from models.user import User
from models.user_credential import UserCredential

class UserRepository:
    @staticmethod
    def get_all_users_active():
        return User.query.filter_by(is_active=True).all()
    
    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return User.query.get_or_404(user_id)
    
    @staticmethod
    def get_credential_by_user_id(user_id: int):
        return UserCredential.query.filter_by(user_id=user_id).first_or_404()
    
    @staticmethod
    def get_email_by_user(email: str):
        return User.query.filter_by(email=email).first()
    