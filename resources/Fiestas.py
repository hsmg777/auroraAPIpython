# Archivo: resources/Fiestas.py
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.Fiestas import Fiestas
from db import db
from schemas.schemas import FiestaSchema  # Importa el esquema desde schemas/Schema.py
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint("Fiestas", __name__, url_prefix="/api/fiestas", description="CRUD fiestas")

# Instancia del esquema
fiesta_schema = FiestaSchema()
fiestas_schema = FiestaSchema(many=True)

# GET /api/fiestas
@blp.route('/')
class FiestasList(MethodView):
    @blp.response(200, FiestaSchema(many=True))  # Define el esquema para la respuesta
    def get(self):
        fiestas = Fiestas.query.all()
        return fiestas
    
    @blp.arguments(FiestaSchema)  # Define el esquema para la carga útil
    @blp.response(201, FiestaSchema)  # Define el esquema para la respuesta
    def post(self, data):
        nueva_fiesta = Fiestas(
            numerodia=data['numerodia'],
            dia=data['dia'],
            nombreFiesta=data['nombreFiesta'],
            descripcion=data['descripcion'],
            fecha=data['fecha']
        )
        db.session.add(nueva_fiesta)
        db.session.commit()
        return nueva_fiesta

# GET, PUT, DELETE /api/fiestas/<int:idFiesta>
@blp.route('/<int:idFiesta>')
class FiestaResource(MethodView):
    @blp.response(200, FiestaSchema)  # Define el esquema para la respuesta
    def get(self, idFiesta):
        fiesta = Fiestas.query.get(idFiesta)
        if fiesta is None:
            abort(404, message="Fiesta no encontrada")
        return fiesta

    @blp.arguments(FiestaSchema)  # Define el esquema para la carga útil
    @blp.response(200, FiestaSchema)  # Define el esquema para la respuesta
    def put(self, data, idFiesta):
        fiesta = Fiestas.query.get(idFiesta)
        if fiesta is None:
            abort(404, message="Fiesta no encontrada")
        
        fiesta.numerodia = data['numerodia']
        fiesta.dia = data['dia']
        fiesta.nombreFiesta = data['nombreFiesta']
        fiesta.descripcion = data['descripcion']
        fiesta.fecha = data['fecha']
        
        db.session.commit()
        return fiesta

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, idFiesta):
        fiesta = Fiestas.query.get(idFiesta)
        if fiesta is None:
            abort(404, message="Fiesta no encontrada")
        db.session.delete(fiesta)
        db.session.commit()
        return '', 204
