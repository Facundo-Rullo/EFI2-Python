from flask import Flask, request
from models import (
    db
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:@localhost/efi2_python'
)
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'cualquier-cosa-re-dificl-espero-aprobar-jajajajaj'

db.init_app(app)

@app.route('/')
def index():
    return 'Hello Fucking World'
