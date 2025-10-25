from flask import jsonify
from models import db
from models.user import User
from repositories.UserRepository import UserRepository
from sqlalchemy.exc import SQLAlchemyError

class UserService:
    def __init__(self):
        self.repo = UserRepository()
        
    def get_users_active(self):
        return self.repo.get_all_users_active()
    
    def get_user_by_id(self, user_id: int):
        return self.repo.get_user_by_id(user_id)
    
    def deactivate_user(self, user_id: int) -> User:
        user = self.repo.get_user_by_id(user_id)

        try:
            user.is_active = False
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Error al eliminar el usuario: {str(e)}")