# Archivo: resources/About.py
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.Politicas import Politicas
from db import db
from schemas.PoliticasSchema import PoliticasSchema  # Importa el esquema desde schemas/AboutSchema.py
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint("Politicas", __name__, url_prefix="/api/politicas", description="CRUD for Politicas")

# Instancia del esquema
politica_schema = PoliticasSchema()
politicas_schema = PoliticasSchema(many=True)

# GET /api/politicas
@blp.route('/')
class PoliticasList(MethodView):
    @blp.response(200, PoliticasSchema(many=True))  # Define el esquema para la respuesta
    def get(self):
        normas = Politicas.query.all()
        return normas

    @blp.arguments(PoliticasSchema)  # Define el esquema para la carga útil
    @blp.response(201, PoliticasSchema)  # Define el esquema para la respuesta
    def post(self, data):
        nueva_politica = Politicas(politica=data['politica'])
        db.session.add(nueva_politica)
        db.session.commit()
        return nueva_politica

# GET, PUT, DELETE /api/about/<int:Id>
@blp.route('/<int:idPolitica>')
class PoliticasResource(MethodView):
    @blp.response(200, PoliticasSchema)  # Define el esquema para la respuesta
    def get(self, idPolitica):
        politica = Politicas.query.get(idPolitica)
        if politica is None:
            abort(404, message="Politicas no encontrado")
        return politica

    @blp.arguments(PoliticasSchema)  # Define el esquema para la carga útil
    @blp.response(200, PoliticasSchema)  # Define el esquema para la respuesta
    def put(self, data, idPolitica):
        politica = Politicas.query.get(idPolitica)
        if politica is None:
            abort(404, message="Politica no encontrado")
        
        politica.politica = data['politica']
        
        db.session.commit()
        return politica

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, idPolitica):
        politica = Politicas.query.get(idPolitica)
        if politica is None:
            abort(404, message="Politica no encontrado")
        db.session.delete(politica)
        db.session.commit()
        return '', 204

