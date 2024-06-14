# Archivo: resources/COntact.py
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.Contact import Contact
from db import db
from schemas.ContactSchema import ContactSchema  # Importa el esquema desde schemas/AboutSchema.py
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint("Contact", __name__, url_prefix="/api/contact", description="CRUD for Contact")

# Instancia del esquema
contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)

# GET /api/contact
@blp.route('/')
class ContactList(MethodView):
    @blp.response(200, contacts_schema)  # Usar contacts_schema para la respuesta de muchos contactos
    def get(self):
        contacts = Contact.query.all()
        return contacts

    @blp.arguments(ContactSchema)  # Define el esquema para la carga útil
    @blp.response(201, ContactSchema)  # Define el esquema para la respuesta
    def post(self, data):
        nuevo_contact = Contact(
            numero=data['numero'],
            correo=data['correo'])
        db.session.add(nuevo_contact)
        db.session.commit()
        return nuevo_contact

# GET, PUT, DELETE /api/contact/<int:idContact>
@blp.route('/<int:idContact>')
class ContactResource(MethodView):
    @blp.response(200, ContactSchema)  # Define el esquema para la respuesta
    def get(self, idContact):
        contact = Contact.query.get(idContact)
        if contact is None:
            abort(404, message="Contact no encontrado")
        return contact
    @blp.arguments(ContactSchema)  # Define el esquema para la carga útil
    @blp.response(200, ContactSchema)  # Define el esquema para la respuesta
    def put(self, data, idContact):
        contact = Contact.query.get(idContact)
        if contact is None:
            abort(404, message="Contact no encontrado")
        
        contact.numero= data['numero']
        contact.correo=data['correo']
        
        db.session.commit()
        return contact

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, idContact):
        contact = Contact.query.get(idContact)
        if contact is None:
            abort(404, message="Contact no encontrado")
        db.session.delete(contact)
        db.session.commit()
        return '', 204

