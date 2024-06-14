from marshmallow import Schema, fields

class FiestaSchema(Schema):
    idFiesta = fields.Int(dump_only=True)  # Solo para serialización
    numerodia = fields.Str(required=True)
    dia = fields.Str(required=True)
    nombreFiesta = fields.Str(required=True)
    descripcion = fields.Str(required=True)
    fecha = fields.Date(required=True, format='%Y-%m-%d')