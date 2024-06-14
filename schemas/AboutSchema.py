from marshmallow import Schema, fields
class AboutSchema(Schema):
    Id = fields.Int(dump_only=True)
    body = fields.Str(required=True)