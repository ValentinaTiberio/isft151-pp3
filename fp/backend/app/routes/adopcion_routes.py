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
    return jsonify(listar_solicitudes())

@adopcion_bp.route("/<int:id>", methods=["PUT"])
def actualizar(id):
    data = request.get_json()
    estado = data.get("estado")
    actualizada = actualizar_estado(id, estado)
    if actualizada:
        return jsonify(actualizada)
    return jsonify({"error": "Solicitud no encontrada"}), 404
