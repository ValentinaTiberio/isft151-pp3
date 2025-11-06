from backend.app.models.animal_model import Animal
from backend.app.models.adopcion_model import Adopcion
from backend.main import db
from sqlalchemy import func

def obtener_estadisticas():
    total_animales = db.session.query(func.count(Animal.id)).scalar()
    total_adopciones = db.session.query(func.count(Adopcion.id)).scalar()

    # Detalle por estado
    animales_por_estado = (
        db.session.query(Animal.estado, func.count(Animal.id))
        .group_by(Animal.estado)
        .all()
    )

    # Lo transformamos a diccionario
    detalle_estado = {estado: cantidad for estado, cantidad in animales_por_estado}

    return {
        "total_animales": total_animales,
        "total_adopciones": total_adopciones,
        "detalle_estado": detalle_estado
    }
