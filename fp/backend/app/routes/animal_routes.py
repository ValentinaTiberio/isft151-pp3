from flask import Blueprint, request, jsonify
from backend.app.services.animal_service import create_animal, list_animals

animal_bp = Blueprint("animal", __name__)

@animal_bp.route("/", methods=["GET"])
def get_animals():
    return jsonify(list_animals())

@animal_bp.route("/", methods=["POST"])
def add_animal():
    data = request.get_json()
    animal = create_animal(data)
    return jsonify(animal), 201
