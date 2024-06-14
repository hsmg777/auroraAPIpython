from db import db
from datetime import datetime

class Galeria(db.Model):
     __tablename__ = 'galeria'
     Id = db.Column(db.Integer, primary_key=True)
     URLimg = db.Column(db.String(), nullable=False)
     nombreArchivo = db.Column(db.String(155), nullable=False)
     MIME = db.Column(db.String(), nullable=False)
     fechaCarga = db.Column(db.Date, nullable=False)
     
     def __init__(self, URLimg, nombreArchivo, MIME, fechaCarga):
         self.URLimg =URLimg
         self.nombreArchivo = nombreArchivo
         self.MIME = MIME
         self.fechaCarga = fechaCarga