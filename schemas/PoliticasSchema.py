from marshmallow import Schema, fields
class PoliticasSchema(Schema):
    idPolitica = fields.Int(dump_only=True)
    politica = fields.Str(required=True)