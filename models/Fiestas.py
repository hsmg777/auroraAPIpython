from db import db
from datetime import datetime

class Fiestas(db.Model):
    __tablename__ = 'fiestas'
    idFiesta = db.Column(db.Integer, primary_key=True)
    numerodia = db.Column(db.String(7), nullable=False)
    dia = db.Column(db.String(7), nullable=False)
    nombreFiesta = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def __init__(self, numerodia, dia, nombreFiesta, descripcion, fecha):
        self.numerodia = numerodia
        self.dia = dia
        self.nombreFiesta = nombreFiesta
        self.descripcion = descripcion
        self.fecha = fecha
