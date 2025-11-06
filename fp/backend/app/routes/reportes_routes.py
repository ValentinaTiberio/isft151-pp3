from flask import Blueprint, jsonify
from backend.app.services.reportes_service import obtener_estadisticas

reportes_bp = Blueprint("reportes", __name__)

@reportes_bp.route("/", methods=["GET"])
def ver_reportes():
    datos = obtener_estadisticas()
    return jsonify(datos)
