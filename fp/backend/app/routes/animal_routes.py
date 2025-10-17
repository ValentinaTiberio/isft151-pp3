from flask import Blueprint, request, jsonify, send_from_directory
from backend.app.services.animal_service import create_animal, list_animals
import os

animal_bp = Blueprint("animals", __name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "..", "..", "uploads")

@animal_bp.route("/", methods=["POST"])
def register_animal():
    data = request.form
    foto = request.files.get("foto")
    animal = create_animal(data, foto)
    return jsonify(animal), 201


@animal_bp.route("/", methods=["GET"])
def get_animals():
    animals = list_animals()
    return jsonify(animals)


# Servir imágenes guardadas
@animal_bp.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
