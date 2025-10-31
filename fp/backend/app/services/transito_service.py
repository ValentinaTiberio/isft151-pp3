from backend.app.models.transito_model import Transito
from backend.app.models.animal_model import Animal
from backend.main import db
import datetime

def crear_transito(animal_id, user_id):
    # Evitar duplicados
    activo = Transito.query.filter_by(animal_id=animal_id, estado="Activo").first()
    if activo:
        return {"error": "Este animal ya tiene un hogar de tránsito activo."}

    transito = Transito(animal_id=animal_id, user_id=user_id)
    db.session.add(transito)

    # Cambiar estado del animal
    animal = Animal.query.get(animal_id)
    if animal:
        animal.estado = "Tránsito"

    db.session.commit()
    return transito.to_dict()

def listar_transitos():
    return [t.to_dict() for t in Transito.query.all()]

def finalizar_transito(id):
    t = Transito.query.get(id)
    if not t:
        return None
    t.estado = "Finalizado"
    t.fecha_fin = datetime.datetime.utcnow()

    # Devolver animal a "En adopción"
    if t.animal:
        t.animal.estado = "En adopción"

    db.session.commit()
    return t.to_dict()
