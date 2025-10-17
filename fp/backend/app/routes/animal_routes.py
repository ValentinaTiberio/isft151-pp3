from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os, datetime

animal_bp = Blueprint("animals", __name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "..", "..", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

animals = []  # Simulamos una "base de datos"

@animal_bp.route("/", methods=["POST"])
def create_animal():
    nombre = request.form.get("nombre")
    especie = request.form.get("especie")
    estado = request.form.get("estado")

    # Guardamos si es que hay imágen
    foto = request.files.get("foto")
    filename = None
    if foto:
        filename = secure_filename(foto.filename)
        foto.save(os.path.join(UPLOAD_FOLDER, filename))

    animal = {
        "id": len(animals) + 1,
        "nombre": nombre,
        "especie": especie,
        "estado": estado,
        "fecha_ingreso": datetime.datetime.now().strftime("%Y-%m-%d"),
        "foto": filename
    }
    animals.append(animal)
    return jsonify(animal), 201


@animal_bp.route("/", methods=["GET"])
def list_animals():
    return jsonify(animals)

# Servir las imágenes guardadas
from flask import send_from_directory
@animal_bp.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
