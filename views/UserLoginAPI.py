from datetime import timedelta
from flask import request, jsonify
from marshmallow import ValidationError
from flask.views import MethodView

from passlib.hash import bcrypt
from flask_jwt_extended import ( 
    create_access_token,
)

from models.user import User

from schemas.LoginSchema import LoginSchema

class UserLoginAPI(MethodView):
    def post(self):
        try: 
            data = LoginSchema().load(request.json)
        except ValidationError as err:
            return {"Error": err.messages}
        
        user = User.query.filter_by(email=data.get("email")).first()
        
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