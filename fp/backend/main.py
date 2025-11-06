from flask import Flask, send_from_directory
from backend.app.db_config import db
import os


def create_app():
    app = Flask(__name__)

    # Configuración base de datos
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rescatepet.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # Blueprints
    from backend.app.routes.user_routes import user_bp
    from backend.app.routes.animal_routes import animal_bp
    from backend.app.routes.adopcion_routes import adopcion_bp
    from backend.app.routes.transito_routes import transito_bp
    from backend.app.routes.reportes_routes import reportes_bp
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(animal_bp, url_prefix="/api/animals")
    app.register_blueprint(adopcion_bp, url_prefix="/api/adopciones")
    app.register_blueprint(transito_bp, url_prefix="/api/transitos")
    app.register_blueprint(reportes_bp, url_prefix="/api/reportes")

    # Carpeta frontend
    FRONTEND_FOLDER = os.path.join(os.path.dirname(__file__), "..", "frontend")

    @app.route("/")
    def home():
        return send_from_directory(FRONTEND_FOLDER, "index.html")

    @app.route("/registro")
    def registro_page():
        return send_from_directory(FRONTEND_FOLDER, "registro.html")

    @app.route("/animales")
    def animales_page():
        return send_from_directory(FRONTEND_FOLDER, "animales.html")
    
    @app.route("/solicitudes")
    def solicitudes_page():
        return send_from_directory(FRONTEND_FOLDER, "solicitudes.html")

    @app.route("/admin/solicitudes")
    def admin_solicitudes_page():
        return send_from_directory(FRONTEND_FOLDER, "admin_solicitudes.html")
    
    @app.route("/admin/reportes")
    def admin_reportes_page():
        return send_from_directory(FRONTEND_FOLDER, "admin_reportes.html")

    @app.route("/<path:path>")
    def static_files(path):
        return send_from_directory(FRONTEND_FOLDER, path)

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
