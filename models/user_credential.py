from . import db # Importamos 'db' desde el __init__.py

class UserCredential(db.Model):
    __tablename__ = "user_credential"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="user") # admin, moderator, user

    user = db.relationship("User", backref=db.backref("credential", uselist=False)) # useList significa que hace una relacion 1 a 1 devuelve un solo objeto.

    def __str__(self) -> str:
        return f"Credenciales para Usuario ID={self.user_id}, role={self.role}"
