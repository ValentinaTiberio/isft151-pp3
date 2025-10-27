from backend.app.db_config import db
import datetime

class Adopcion(db.Model):
    __tablename__ = "adopciones"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey("animal.id"), nullable=False)
    fecha_solicitud = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    estado = db.Column(db.String(20), default="Pendiente")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "animal_id": self.animal_id,
            "fecha_solicitud": self.fecha_solicitud.strftime("%Y-%m-%d %H:%M"),
            "estado": self.estado
        }
