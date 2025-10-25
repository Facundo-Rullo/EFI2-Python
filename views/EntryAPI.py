from flask import request, jsonify
from marshmallow import ValidationError
from flask.views import MethodView
from flask_jwt_extended import ( 
    jwt_required,
    get_jwt,
    get_jwt_identity
)

from models import db
from models.user import User
from models.user_credential import UserCredential
from models.entry import Entry
from models.comment import Comment
from models.category import Category

from schemas.EntrySchema import EntrySchema
from schemas.EntrySchema import EntrySchema

from decorators.RoleRequired import role_required

from service.EntryService import EntryService

class EntryAPI(MethodView):
    def __init__(self):
            self.service = EntryService()
            
    def get(self):
        entries = self.service.get_public_posts()
        return EntrySchema(many=True).dump(entries)

    @jwt_required()
    @role_required("user")
    def post(self):
        
        try:
            data = EntrySchema().load(request.json)
        except ValidationError as err:
            return jsonify({"Error": err.messages})
        
        current_user_id = get_jwt_identity()
        
        try: 
            new_entry = self.service.create_entry(data, current_user_id)
            return EntrySchema().dump(new_entry), 201
        except ValueError as e:
            return jsonify({"Error": str(e)}), 500
        except Exception as e:
            return jsonify({"Error": f"Error inesperado: {str(e)}"}), 500
        
    
    