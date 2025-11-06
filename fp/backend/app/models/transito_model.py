from backend.app.db_config import db
from datetime import datetime

class Transito(db.Model):
    __tablename__ = 'transitos'

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    direccion = db.Column(db.String(120), nullable=False)
    duracion_dias = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), default='Pendiente')
    fecha_solicitud = db.Column(db.DateTime, default=datetime.now)

    # Relaciones correctas
    animal = db.relationship('Animal', backref='transitos')
    usuario = db.relationship('User', backref='transitos')
