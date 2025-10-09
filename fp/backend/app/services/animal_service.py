from backend.app.models.animal import Animal
from datetime import datetime

# simulación de base de datos
animals = []

def create_animal(data):
    animal = Animal(
        id=len(animals) + 1,
        nombre=data["nombre"],
        especie=data["especie"],
        estado=data.get("estado", "Rescatado"),
        fecha_ingreso=datetime.now().strftime("%Y-%m-%d")
    )
    animals.append(animal)
    return animal.to_dict()

def list_animals():
    return [a.to_dict() for a in animals]
