from flask.views import MethodView
from flask_jwt_extended import ( 
    jwt_required,
)

from models.user import User

from schemas.UserSchema import UserSchema

from decorators.RoleRequired import role_required

class ListUsersAPI(MethodView):
    @jwt_required()
    @role_required("admin")
    def get(self):
        users = User.query.all()
        return UserSchema(many=True).dump(users) 