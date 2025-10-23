from marshmallow import Schema, fields, validate

class UserCredentialSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    role = fields.Str(
        required=True,
        validate=validate.OneOf(["user", "moderator", "admin"]) #Valido que solo se acepten estos 3
        )
    
    