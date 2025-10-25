from marshmallow import Schema, fields

class RegisterSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)