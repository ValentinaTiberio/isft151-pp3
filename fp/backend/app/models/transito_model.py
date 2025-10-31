from backend.app.db_config import db
import datetime

class Transito(db.Model):
    __tablename__ = "transitos"

    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey("animal.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    fecha_inicio = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    fecha_fin = db.Column(db.DateTime, nullable=True)
    estado = db.Column(db.String(20), default="Activo")

    animal = db.relationship("Animal", backref="transitos", lazy=True)
    user = db.relationship("User", backref="transitos", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "animal_id": self.animal_id,
            "animal_nombre": self.animal.nombre if self.animal else None,
            "user_id": self.user_id,
            "user_nombre": self.user.username if self.user else None,
            "fecha_inicio": self.fecha_inicio.strftime("%Y-%m-%d %H:%M"),
            "fecha_fin": self.fecha_fin.strftime("%Y-%m-%d %H:%M") if self.fecha_fin else None,
            "estado": self.estado
        }
