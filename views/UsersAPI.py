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
        return UserSchema().dump(user) 
    
    @jwt_required()
    @role_required("admin") #Delete logico
    def delete(self, user_id):
        try:
            self.service.deactivate_user(user_id) 
            return jsonify({"message": "Usuario eliminado correctamente"})
        except ValidationError as err: 
            return jsonify({"Error": err.messages})
       
class UpdateRoleAPI(MethodView):
    def __init__(self):
        self.service = UserService()
    @jwt_required()
    @role_required("admin")
    def patch(self, user_id):
        try:
            data = UserCredentialSchema(partial=True).load(request.json) 
            new_role = data.get('role')
        except ValidationError as err: 
            return jsonify({"Error": err.messages}), 400 
        
        try:
            update_role = self.service.update_role(user_id, new_role)
            return UserSchema().dump(update_role)
        except ValueError as e: 
            return jsonify({"Error": str(e)}), 500
        except Exception as e: 
            return jsonify({"error": str(e)}), 404
            
            
        