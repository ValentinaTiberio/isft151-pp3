from flask import Blueprint, jsonify, request
from backend.app.services import transito_service

transito_bp = Blueprint('transito_bp', __name__)

@transito_bp.route('/', methods=['GET'])
def obtener_todos():
    transitos = transito_service.obtener_todos()
    return jsonify([{
        "id": t.id,
        "animal_id": t.animal_id,
        "animal_nombre": t.animal.nombre if t.animal else None,
        "usuario_nombre": t.usuario.username if t.usuario else None,  # ← agregado
        "user_id": t.user_id,
        "direccion": t.direccion,
        "duracion_dias": t.duracion_dias,
        "estado": t.estado,
        "fecha_solicitud": t.fecha_solicitud.strftime("%Y-%m-%d %H:%M")
    } for t in transitos])


@transito_bp.route('/usuario/<int:user_id>', methods=['GET'])
def obtener_por_usuario(user_id):
    transitos = transito_service.obtener_por_usuario(user_id)
    return jsonify([{
        "id": t.id,
        "animal_id": t.animal_id,
        "animal_nombre": t.animal.nombre if t.animal else None,
        "direccion": t.direccion,
        "duracion_dias": t.duracion_dias,
        "estado": t.estado,
        "fecha_solicitud": t.fecha_solicitud.strftime("%Y-%m-%d %H:%M")
    } for t in transitos])

@transito_bp.route('/', methods=['POST'])
def crear_transito():
    data = request.get_json()
    t = transito_service.crear_transito(data)
    return jsonify({"mensaje": "Tránsito creado correctamente", "id": t.id})

@transito_bp.route('/<int:id>', methods=['PUT'])
def actualizar_estado(id):
    data = request.get_json()
    nuevo_estado = data.get("estado")

    from backend.app.models.transito_model import Transito
    t = Transito.query.get(id)

    if not t:
        return jsonify({"error": "Transito no encontrado"}), 404

    t.estado = nuevo_estado
    from backend.app.db_config import db
    db.session.commit()

    return jsonify({"mensaje": f"Estado actualizado a {nuevo_estado}"}), 200

