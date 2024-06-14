from db import db

class Politicas(db.Model):
     __tablename__ = 'politicas'
     idPolitica = db.Column(db.Integer, primary_key=True)
     politica = db.Column(db.String(150), nullable=False)
     
     
     def __init__(self, politica):
         self.politica =politica