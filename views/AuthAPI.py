from datetime import timedelta
from flask import request, jsonify
from marshmallow import ValidationError
from flask.views import MethodView
from passlib.hash import bcrypt

from flask_jwt_extended import ( 
    create_access_token,
)

from models import db
from models.user import User
from models.user_credential import UserCredential
from models.entry import Entry
from models.comment import Comment
from models.category import Category

from schemas.RegisterSchema import RegisterSchema
from schemas.UserSchema import UserSchema
from schemas.LoginSchema import LoginSchema

from service.UserService import UserService

class UserRegisterAPI(MethodView):
    def post(self):
        try:
            data = RegisterSchema().load(request.json)
        except ValidationError as err:
            return {"Error": err.messages}
        
        if User.query.filter_by(email=data.get('email')).first():
            return jsonify({"Error": "Email en uso, ingrese otro!"}), 409

        new_user = User(
            username = data.get("username"),
            email = data.get("email")
        )
        db.session.add(new_user)
        db.session.flush()
        
        password_hash = bcrypt.hash(data.get("password"))
        credentials = UserCredential(
            user_id = new_user.id,
            password_hash = password_hash
        )
        db.session.add(credentials)
        db.session.commit()
        
        return UserSchema().dump(new_user) #Consultar si esta bien delvolver esto
    

class UserLoginAPI(MethodView):
    def __init__(self):
        self.service = UserService()
        
    def post(self):
        try: 
            data = LoginSchema().load(request.json)
        except ValidationError as err:
            return {"Error": err.messages}
        
        verify_email = data.get("email")
        user = self.service.get_email_user(verify_email)
        # user = User.query.filter_by(email=data.get("email")).first()
        
        if not user or not user.credential:
            return jsonify({"Error": "El usuario no posee credenciales!"}), 409
        
        if not bcrypt.verify(data.get('password') , user.credential.password_hash):
            return jsonify({"Error": "Credenciales Invalidas!"}), 409
        
        additional_claims = {
            "email": user.email,
            "role": user.credential.role,
            "name": user.username
        }
        identity = str(user.id)
        token = create_access_token(
            identity = identity,
            additional_claims = additional_claims,
            expires_delta = timedelta(hours=24)
        )
        
        return jsonify(access_token=token)