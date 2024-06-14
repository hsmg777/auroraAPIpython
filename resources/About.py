# Archivo: resources/About.py
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.About import About
from db import db
from schemas.AboutSchema import AboutSchema  # Importa el esquema desde schemas/AboutSchema.py
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint("About", __name__, url_prefix="/api/about", description="CRUD for About")

# Instancia del esquema
about_schema = AboutSchema()
abouts_schema = AboutSchema(many=True)

# GET /api/about
@blp.route('/')
class AboutList(MethodView):
    @blp.response(200, AboutSchema(many=True))  # Define el esquema para la respuesta
    def get(self):
        abouts = About.query.all()
        return abouts

    @blp.arguments(AboutSchema)  # Define el esquema para la carga útil
    @blp.response(201, AboutSchema)  # Define el esquema para la respuesta
    def post(self, data):
        nuevo_about = About(body=data['body'])
        db.session.add(nuevo_about)
        db.session.commit()
        return nuevo_about

# GET, PUT, DELETE /api/about/<int:Id>
@blp.route('/<int:Id>')
class AboutResource(MethodView):
    @blp.response(200, AboutSchema)  # Define el esquema para la respuesta
    def get(self, Id):
        about = About.query.get(Id)
        if about is None:
            abort(404, message="About no encontrado")
        return about

    @blp.arguments(AboutSchema)  # Define el esquema para la carga útil
    @blp.response(200, AboutSchema)  # Define el esquema para la respuesta
    def put(self, data, Id):
        about = About.query.get(Id)
        if about is None:
            abort(404, message="About no encontrado")
        
        about.body = data['body']
        
        db.session.commit()
        return about

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, Id):
        about = About.query.get(Id)
        if about is None:
            abort(404, message="About no encontrado")
        db.session.delete(about)
        db.session.commit()
        return '', 204

