from backend.app.db_config import db
from datetime import datetime

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    especie = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    foto = db.Column(db.String(200))
    fecha_ingreso = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especie": self.especie,
            "estado": self.estado,
            "foto": self.foto,
            "fecha_ingreso": self.fecha_ingreso.strftime("%Y-%m-%d")
        }
