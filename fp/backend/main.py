from flask import Flask, send_from_directory
import os
from backend.app.routes.user_routes import user_bp
from backend.app.routes.animal_routes import animal_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(animal_bp, url_prefix="/api/animals")

    # Ruta a la carpeta frontend (está al mismo nivel que backend)
    FRONTEND_FOLDER = os.path.join(os.path.dirname(__file__), "..", "frontend")

    # Servir index.html en "/"
    @app.route("/")
    def home():
        return send_from_directory(FRONTEND_FOLDER, "index.html")
    
    @app.route("/animales")
    def animales_page():
        return send_from_directory(FRONTEND_FOLDER, "animales.html")
    
    @app.route("/inicio")
    def inicio_page():
        return send_from_directory(FRONTEND_FOLDER, "inicio.html")


    # Servir archivos estáticos del frontend (JS, CSS, imágenes, etc.)
    @app.route("/<path:path>")
    def static_files(path):
        return send_from_directory(FRONTEND_FOLDER, path)

    @app.route("/api/health")
    def health():
        return {"status": "ok"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
