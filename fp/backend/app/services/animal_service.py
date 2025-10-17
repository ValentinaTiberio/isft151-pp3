from backend.app.models.animal_model import Animal
from backend.main import db
from werkzeug.utils import secure_filename
import os, datetime

# Carpeta donde se guardan las fotos
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "..", "..", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def create_animal(data, foto):
    """Crea un nuevo animal en la base de datos"""
    filename = None

    # Si se subió una foto, la guardamos
    if foto:
        filename = secure_filename(foto.filename)
        foto.save(os.path.join(UPLOAD_FOLDER, filename))

    animal = Animal(
        nombre=data.get("nombre"),
        especie=data.get("especie"),
        estado=data.get("estado"),
        foto=filename,
        fecha_ingreso=datetime.datetime.now()
    )
    db.session.add(animal)
    db.session.commit()

    return animal.to_dict()


def list_animals():
    """Devuelve todos los animales registrados"""
    return [a.to_dict() for a in Animal.query.all()]
