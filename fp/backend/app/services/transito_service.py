from backend.app.models.transito_model import Transito
from backend.app.db_config import db

def crear_transito(data):
    nuevo = Transito(
        animal_id=data['animal_id'],
        user_id=data['user_id'],
        direccion=data['direccion'],
        duracion_dias=data['duracion'],
        estado='Pendiente'
    )
    db.session.add(nuevo)
    db.session.commit()
    return nuevo

def obtener_todos():
    return Transito.query.all()

def obtener_por_usuario(user_id):
    return Transito.query.filter_by(user_id=user_id).all()

def cambiar_estado(id, nuevo_estado):
    t = Transito.query.get(id)
    if not t:
        return None
    t.estado = nuevo_estado
    db.session.commit()
    return t
