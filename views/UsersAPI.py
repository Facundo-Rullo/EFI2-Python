from flask import request, jsonify
from marshmallow import ValidationError
from flask.views import MethodView
from flask_jwt_extended import ( 
    jwt_required,
)


from models import db
from models.user import User
from models.user_credential import UserCredential
from models.entry import Entry
from models.comment import Comment
from models.category import Category

from schemas.UserSchema import UserSchema
from schemas.UserCredentialSchema import UserCredentialSchema

from decorators.RoleRequired import role_required

from service.UserService import UserService

class ListUsersAPI(MethodView):
    def __init__(self):
            self.service = UserService()
            
    @jwt_required()
    @role_required("admin")
    def get(self):
        users = self.service.get_users_active()
        return UserSchema(many=True).dump(users) 
    
    
class OneUserAPI(MethodView):
    def __init__(self):
            self.service = UserService()
            
    @jwt_required()
    @role_required("admin", "user")
    def get(self, user_id):
        user = self.service.get_user_by_id(user_id)
        # users = User.query.get_or_404(user_id)
        return UserSchema().dump(user) 
    
    @jwt_required()
    @role_required("admin")
    def patch(self, user_id):
        user = User.query.get_or_404(user_id)
        try:
            data = UserSchema(partial=True).load(request.json) 
            if 'is_active' in data:
                user.is_active = data.get("is_active")
            
            db.session.commit()
            return jsonify({"message": "Usuario eliminado correctamente"})
        except ValidationError as err: 
            return jsonify({"Error": err.messages})
    
       
class UpdateRoleAPI(MethodView):
    @jwt_required()
    @role_required("admin")
    def patch(self, user_id):
        credentials = UserCredential.query.filter_by(user_id=user_id).first_or_404()
        try:
            data = UserCredentialSchema(partial=True).load(request.json) 
            if 'role' in data:
                credentials.role = data.get("role")
            
            db.session.commit()
            return UserSchema().dump(credentials.user)
        except ValidationError as err: 
            return jsonify({"Error": err.messages})
        