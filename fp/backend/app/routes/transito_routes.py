from flask import Blueprint, request, jsonify
from backend.app.services.transito_service import crear_transito, listar_transitos, finalizar_transito

transito_bp = Blueprint("transitos", __name__)

@transito_bp.route("/", methods=["POST"])
def crear():
    data = request.get_json()
    animal_id = data.get("animal_id")
    user_id = data.get("user_id")
    nuevo = crear_transito(animal_id, user_id)
    return jsonify(nuevo), 201

@transito_bp.route("/", methods=["GET"])
def listar():
    return jsonify(listar_transitos())

@transito_bp.route("/<int:id>/finalizar", methods=["PUT"])
def finalizar(id):
    actualizado = finalizar_transito(id)
    if actualizado:
        return jsonify(actualizado)
    return jsonify({"error": "Transito no encontrado"}), 404
