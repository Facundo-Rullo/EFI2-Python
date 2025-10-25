from datetime import datetime
from marshmallow import Schema, fields

class EntrySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    is_published = fields.Bool(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user_id = fields.Int(dump_only=True) 
    
    # comments = fields.List(fields.Nested(CommentSchema), dump_only=True)  # Aquí usamos otro schema para comentarios
    # categories = fields.List(fields.Nested(CategorySchema))  # Aquí usamos un schema para categorías
