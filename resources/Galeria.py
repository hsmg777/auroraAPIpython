# Archivo: resources/Galeria.py
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.Galeria import Galeria
from db import db
from schemas.GaleriaSchema import GaleriaSchema 
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint("Galeria", __name__, url_prefix="/api/galeria", description="CRUD Galeria")

# Instancia del esquema
galeria_schema = GaleriaSchema()
galerias_schema = GaleriaSchema(many=True)


# GET /api/galeria
@blp.route('/')
class GaleriaList(MethodView):
    @blp.response(200, GaleriaSchema(many=True))  # Define el esquema para la respuesta
    def get(self):
        galerias = Galeria.query.all()
        return galerias
    
    @blp.arguments(GaleriaSchema)  # Define el esquema para la carga útil
    @blp.response(201, GaleriaSchema)  # Define el esquema para la respuesta
    def post(self, data):
        nueva_galeria = Galeria(
            URLimg=data['URLimg'],
            nombreArchivo=data['nombreArchivo'],
            MIME=data['MIME'],
            fechaCarga=data['fechaCarga']
        )
        db.session.add(nueva_galeria)
        db.session.commit()
        return nueva_galeria

# GET, PUT, DELETE /api/galeria/<int:Id>
@blp.route('/<int:Id>')
class GaleriaResource(MethodView):
    @blp.response(200, GaleriaSchema)  # Define el esquema para la respuesta
    def get(self, Id):
        galeria = Galeria.query.get(Id)
        if galeria is None:
            abort(404, message="Galeria no encontrada")
        return galeria

    @blp.arguments(GaleriaSchema)  # Define el esquema para la carga útil
    @blp.response(200, GaleriaSchema)  # Define el esquema para la respuesta
    def put(self, data, Id):
        galeria = Galeria.query.get(Id)
        if galeria is None:
            abort(404, message="Galeria no encontrada")
        
        galeria.URLimg = data['URLimg']
        galeria.nombreArchivo = data['nombreArchivo']
        galeria.MIME = data['MIME']
        galeria.fechaCarga = data['fechaCarga']        
        db.session.commit()
        return galeria

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, Id):
        galeria = Galeria.query.get(Id)
        if galeria is None:
            abort(404, message="Galeria no encontrada")
        db.session.delete(galeria)
        db.session.commit()
        return '', 204

