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

from schemas.RegisterSchema import RegisterSchema
from schemas.UserSchema import UserSchema

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