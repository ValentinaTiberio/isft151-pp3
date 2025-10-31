from flask import Blueprint, request, jsonify
from backend.app.services.user_service import create_user, authenticate_user, list_users
import jwt, datetime

SECRET_KEY = "rescatepet_secret"

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = create_user(data)
    return jsonify(user), 201

@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = authenticate_user(data["email"], data["password"])
    if not user:
        return jsonify({"error": "Credenciales inválidas"}), 401

    token = jwt.encode(
        {"id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)},
        SECRET_KEY,
        algorithm="HS256"
    )

    #Ahora devolvemos también los datos del usuario logueado
    return jsonify({
        "token": token,
        "user": user.to_dict()
    })


@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(list_users())
    
