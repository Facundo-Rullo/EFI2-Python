from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from models import db

from views.UserRegisterAPI import UserRegisterAPI


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
    '/register',
    view_func=UserRegisterAPI.as_view("register_api"),
    methods=['POST']
)
