from db import db

class Reservas(db.Model):
    __tablename__ = 'Reservas'
    idReserva = db.Column(db.Integer, primary_key=True)
    idFiesta = db.Column(db.Integer, nullable=False)
    vaucher = db.Column(db.String(50), nullable=False)
    nombreReserva = db.Column(db.String(50), nullable=False)
    apellidoReserva = db.Column(db.String(50), nullable=False)
    numeroPersonas = db.Column(db.String(10), nullable=False)
    hora = db.Column(db.String(20), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    
    def __init__(self, vaucher, nombreReserva, apellidoReserva, numeroPersonas, hora, telefono):
        self.vaucher = vaucher
        self.nombreReserva = nombreReserva
        self.apellidoReserva = apellidoReserva
        self.numeroPersonas = numeroPersonas
        self.hora = hora
        self.telefono = telefono
