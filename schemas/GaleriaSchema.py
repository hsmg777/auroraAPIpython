from marshmallow import Schema, fields
class GaleriaSchema(Schema):
    Id = fields.Int(dump_only=True)
    URLimg = fields.Str(required=True)
    nombreArchivo = fields.Str(required=True)
    MIME = fields.Str(required=True)
    fechaCarga = fields.Date(required=True, format='%Y-%m-%d')