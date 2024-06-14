from marshmallow import Schema, fields

class ContactSchema(Schema):
    idContact = fields.Int(dump_only=True)  # Incluir el campo idContact en la respuesta
    numero = fields.Str(required=True)
    correo = fields.Str(required=True)
