from flask import Flask
from backend.app.routes.user_routes import user_bp 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp, url_prefix="/api/users")

    @app.route("/api/health")
    def health():
        return {"status": "ok"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
