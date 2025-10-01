from backend.app.models.user import User

users = []  # simulación de base de datos

def create_user(data):
    user = User(len(users) + 1, data["username"], data["email"], data["password"], data.get("role", "user"))
    users.append(user)
    return user.to_dict()

def authenticate_user(email, password):
    for u in users:
        if u.email == email and u.check_password(password):
            return u
    return None

def list_users():
    return [u.to_dict() for u in users]
