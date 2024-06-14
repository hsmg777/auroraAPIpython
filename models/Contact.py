from db import db

class Contact(db.Model):
     __tablename__ = 'contact'
     idContact = db.Column(db.Integer, primary_key=True)
     numero = db.Column(db.String(15), nullable=False)
     correo = db.Column(db.String(50), nullable=False)
     
     def __init__(self, numero, correo):
         self.numero = numero
         self.correo = correo
 
 
