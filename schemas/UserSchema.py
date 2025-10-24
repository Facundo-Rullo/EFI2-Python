from marshmallow import Schema, fields
from .UserCredentialSchema import UserCredentialSchema
    
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(required=True)
    is_active = fields.Boolean(required=True)
    
    credential = fields.Nested(
        UserCredentialSchema,
        exclude=("id", "user_id",), 
        dump_only=True
    )
   
    #Actualizar esto despues para agregar las entradas y comentarios
    
    