from flask.views import MethodView
from flask_jwt_extended import ( 
    jwt_required,
)

from models.user import User

from schemas.UserSchema import UserSchema

from decorators.RoleRequired import role_required

class ListOneUserAPI(MethodView):
    @jwt_required()
    @role_required("admin")
    def get(self, user_id):
        users = User.query.get_or_404(user_id)
        return UserSchema().dump(users) 