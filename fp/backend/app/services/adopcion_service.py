from backend.app.models.adopcion_model import Adopcion
from backend.main import db

def crear_solicitud(user_id, animal_id):
    # Verifica si ya existe una solicitud para ese usuario y animal
    existente = Adopcion.query.filter_by(user_id=user_id, animal_id=animal_id).first()
    if existente:
        return {"error": "Ya solicitaste adoptar este animal."}

    adopcion = Adopcion(user_id=user_id, animal_id=animal_id)
    db.session.add(adopcion)
    db.session.commit()
    return adopcion.to_dict()

def listar_solicitudes():
    return [a.to_dict() for a in Adopcion.query.all()]

def actualizar_estado(id, nuevo_estado):
    adopcion = Adopcion.query.get(id)
    if adopcion:
        adopcion.estado = nuevo_estado
        db.session.commit()
        return adopcion.to_dict()
    return None
