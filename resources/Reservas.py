# Archivo: resources/About.py
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.Reservas import Reservas
from db import db
from schemas.ReservasSchema import ReservasSchema  # Importa el esquema desde schemas/AboutSchema.py
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint("Reservas", __name__, url_prefix="/api/reservas", description="CRUD for reservas")

# Instancia del esquema
reserva_schema = ReservasSchema()
reservas_schema = ReservasSchema(many=True)

# GET /api/reservas
@blp.route('/')
class ReservasList(MethodView):
    @blp.response(200, ReservasSchema(many=True))  # Define el esquema para la respuesta
    def get(self):
        reservas = Reservas.query.all()
        return reservas

    @blp.arguments(ReservasSchema)
    @blp.response(201, ReservasSchema)
    def post(self, data):
        nueva_reserva = Reservas(
            idFiesta=data['idFiesta'],
            vaucher=data['vaucher'],
            nombreReserva=data['nombreReserva'],
            apellidoReserva=data['apellidoReserva'],
            numeroPersonas=data['numeroPersonas'],
            hora=data['hora'],
            telefono=data['telefono']
        )
        db.session.add(nueva_reserva)
        db.session.commit()
        return nueva_reserva

# GET, PUT, DELETE /api/about/<int:Id>
@blp.route('/<int:idReserva>')
class ReservaResource(MethodView):
    @blp.response(200, ReservasSchema)  # Define el esquema para la respuesta
    def get(self, idReserva):
        reserva = Reservas.query.get(idReserva)
        if reserva is None:
            abort(404, message="Reserva no encontrado")
        return reserva

    @blp.arguments(ReservasSchema)  # Define el esquema para la carga útil
    @blp.response(200, ReservasSchema)  # Define el esquema para la respuesta
    def put(self, data, idReserva):
        reserva = Reservas.query.get(idReserva)
        if reserva is None:
            abort(404, message="Reserva no encontrado")
        
        reserva.idFiesta =data['idFiesta'],
        reserva.vaucher=data['vaucher'],
        reserva.nombreReserva=data['nombreReserva'],
        reserva.apellidoReserva=data['apellidoReserva'],
        reserva.numeroPersonas=data['numeroPersonas'],
        reserva.hora=data['hora'],
        reserva.telefono=data['telefono']
        
        
        db.session.commit()
        return reserva

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, idReserva):
        reserva = Reservas.query.get(idReserva)
        if reserva is None:
            abort(404, message="Reserva no encontrado")
        db.session.delete(reserva)
        db.session.commit()
        return '', 204

# GET /api/reservas/GetAllIdFiesta/<int:idFiesta>
@blp.route('/GetAllIdFiesta/<int:idFiesta>')
class ReservaByIdFiesta(MethodView):
    @blp.response(200, ReservasSchema(many=True))
    def get(self, idFiesta):
        reservas = Reservas.query.filter_by(idFiesta=idFiesta).all()
        if not reservas:
            abort(404, message="No se encontraron reservas para la fiesta con el ID proporcionado.")
        return reservas