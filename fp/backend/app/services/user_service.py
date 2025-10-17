from backend.app.models.user_model import User
from backend.main import db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(data):
    hashed_password = generate_password_hash(data["password"])
    user = User(username=data["username"], email=data["email"], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user
    return None

def list_users():
    return [u.to_dict() for u in User.query.all()]
