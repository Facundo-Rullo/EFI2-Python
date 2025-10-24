from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from models import db

from views.AuthAPI import (
    UserRegisterAPI,
    UserLoginAPI
)
from views.UsersAPI import (
    ListUsersAPI,
    OneUserAPI,
    UpdateRoleAPI,
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:@localhost/efi2_python'
)
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'cualquier-cosa-re-dificl-espero-aprobar-jajajajaj'

jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)

app.add_url_rule(
    '/api/register',
    view_func=UserRegisterAPI.as_view("register_api"),
    methods=['POST']
)

app.add_url_rule(
    '/api/login',
    view_func=UserLoginAPI.as_view("login_api"),
    methods=['POST']
)

app.add_url_rule(
    '/api/users',
    view_func=ListUsersAPI.as_view("users_api"),
    methods=['GET']
)

app.add_url_rule(
    '/api/users/<int:user_id>',
    view_func=OneUserAPI.as_view("one_user_api"),
    methods=['GET', 'PATCH']
)

app.add_url_rule(
    '/api/users/<int:user_id>/role',
    view_func=UpdateRoleAPI.as_view("update_role_api"),
    methods=['PATCH']
)

