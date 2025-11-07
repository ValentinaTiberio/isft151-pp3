from flask import Blueprint, request, jsonify
from backend.app.services.adopcion_service import crear_solicitud, listar_solicitudes, actualizar_estado

adopcion_bp = Blueprint("adopciones", __name__)

@adopcion_bp.route("/", methods=["POST"])
def crear():
    data = request.get_json()
    user_id = data.get("user_id")
    animal_id = data.get("animal_id")
    nueva = crear_solicitud(user_id, animal_id)
    return jsonify(nueva), 201

@adopcion_bp.route("/", methods=["GET"])
def listar():
    from backend.app.models.adopcion_model import Adopcion
    adopciones = Adopcion.query.all()
    return jsonify([{
        "id": a.id,
        "animal_id": a.animal_id,
        "animal_nombre": a.animal.nombre if a.animal else None,
        "usuario_nombre": a.user.username if a.user else None,
        "estado": a.estado,
        "fecha_solicitud": a.fecha_solicitud.strftime("%Y-%m-%d %H:%M")
    } for a in adopciones])

@adopcion_bp.route("/<int:id>", methods=["PUT"])
def actualizar(id):
    data = request.get_json()
    estado = data.get("estado")
    actualizada = actualizar_estado(id, estado)
    if actualizada:
        return jsonify(actualizada)
    return jsonify({"error": "Solicitud no encontrada"}), 404

@adopcion_bp.route("/usuario/<int:user_id>", methods=["GET"])
def listar_por_usuario(user_id):
    from backend.app.models.adopcion_model import Adopcion
    solicitudes = Adopcion.query.filter_by(user_id=user_id).all()
    return jsonify([s.to_dict() for s in solicitudes])
