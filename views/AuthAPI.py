from datetime import timedelta
from flask import request, jsonify
from marshmallow import ValidationError
from flask.views import MethodView
from passlib.hash import bcrypt

from flask_jwt_extended import ( 
    create_access_token,
)

from schemas.RegisterSchema import RegisterSchema
from schemas.UserSchema import UserSchema
from schemas.LoginSchema import LoginSchema

from service.UserService import UserService

class UserRegisterAPI(MethodView):
    def __init__(self):
        self.service = UserService()
        
    def post(self):
        try:
            data = RegisterSchema().load(request.json)
        except ValidationError as err:
            return {"Erro2r": err.messages}, 400
        try:
            new_user = self.service.register_user(data)
            return UserSchema().dump(new_user)
        
        except ValueError as e: 
            if "El email ya está en uso" in str(e):
                return jsonify({"Error": str(e)}), 409
            else: 
                return jsonify({"Error": str(e)}), 500
        except Exception as e: 
            return jsonify({"Error": f"Error inesperado: {str(e)}"}), 500
            
                

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