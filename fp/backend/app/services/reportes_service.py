from backend.app.models.animal_model import Animal
from backend.app.models.adopcion_model import Adopcion
from backend.app.models.transito_model import Transito

def obtener_estadisticas():
    total_animales = Animal.query.count()
    total_adopciones = Adopcion.query.filter_by(estado="Aprobada").count()
    total_transitos = Transito.query.filter_by(estado="Aprobado").count()

    return {
        "animales": total_animales,
        "adopciones": total_adopciones,
        "transitos": total_transitos
    }
