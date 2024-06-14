from db import db

class About(db.Model):
    __tablename__ = 'about'
    Id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)
    
    def __init__(self, body):
        self.body = body
