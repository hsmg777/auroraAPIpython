from marshmallow import Schema, fields
class ReservasSchema(Schema):
    idReserva = fields.Int(dump_only=True)
    idFiesta = fields.Int(dumpl_only=True)
    vaucher =fields.Str(required=True)
    nombreReserva =fields.Str(required=True)
    apellidoReserva =fields.Str(required=True)
    numeroPersonas =fields.Str(required=True)
    hora =fields.Str(required=True)
    telefono =fields.Str(required=True)
    