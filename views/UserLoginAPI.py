from flask import request, jsonify
from marshmallow import ValidationError
from flask.views import MethodView
from passlib.hash import bcrypt

from models import db
from models.user import User
from models.user_credential import UserCredential
from models.entry import Entry
from models.comment import Comment
from models.category import Category

from schemas.LoginSchema import LoginSchema
from schemas.UserSchema import UserSchema

class UserLoginAPI(MethodView):
    def post(self):
        try: 
            data = LoginSchema().load(request.json)
        except ValidationError as err:
            return {"Error": err.messages}
        
        user = User.query.filter_by(email=data.get("email")).first()
        
        if not user or user.credential:
            return jsonify({"Error": "El usuario no posee credenciales!"})