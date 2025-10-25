from models import db
from models.user import User
from models.user_credential import UserCredential
from repositories.UserRepository import UserRepository
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import bcrypt

class UserService:
    def __init__(self):
        self.repo = UserRepository()
        
    def get_users_active(self):
        return self.repo.get_all_users_active()
    
    def get_user_by_id(self, user_id: int):
        return self.repo.get_user_by_id(user_id)
    
    def get_email_user(self, email: str):
        return self.repo.get_email_by_user(email)
    
    def update_role(self, user_id: int, new_role: str) -> User:
            
            credential = self.repo.get_credential_by_user_id(user_id)

            try:
                credential.role = new_role
                db.session.commit()
                return credential.user
            except SQLAlchemyError as e:
                db.session.rollback()
                raise ValueError(f"Error al actualizar el rol: {str(e)}")
    
    def register_user(self, data: dict) -> User:
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')

        if self.repo.get_email_by_user(email):
            raise ValueError("El email ya está en uso") 

        new_user = User(username=username, email=email)

        password_hash = bcrypt.hash(password)
        credentials = UserCredential(password_hash=password_hash)
        credentials.user = new_user

        self.repo.add_user_with_credentials(new_user, credentials)

        try:
            db.session.commit()
            return new_user 
        except SQLAlchemyError as err:
            db.session.rollback()
            raise ValueError(f"Error al registrar el usuario: {str(err)}")

    def deactivate_user(self, user_id: int) -> User:
        user = self.repo.get_user_by_id(user_id)

        try:
            user.is_active = False
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise ValueError(f"Error al eliminar el usuario: {str(e)}")