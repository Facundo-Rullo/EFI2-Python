from datetime import timedelta
from flask import request, jsonify
from marshmallow import ValidationError
from flask.views import MethodView

from passlib.hash import bcrypt
from flask_jwt_extended import ( 
    create_access_token,
    jwt_required,
)

from schemas.UserCredentialSchema import UserCredentialSchema
from schemas.UserSchema import UserSchema

from models import db
from models.user_credential import UserCredential

from decorators.RoleRequired import role_required

class UpdateRoleAPI(MethodView):
    @jwt_required()
    @role_required("admin")
    def put(self, user_id):
        credentials = UserCredential.query.filter_by(user_id=user_id).first_or_404()
        try:
            data = UserCredentialSchema().load(request.json) 
            credentials.role = data.get("role")
            
            db.session.commit()
            return UserSchema().dump(credentials.user)
        except ValidationError as err: 
            return jsonify({"Error": err.messages})
        