class Animal:
    def __init__(self, id, nombre, especie, estado, fecha_ingreso):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.estado = estado            # "Rescatado", "En tratamiento", "Listo para adopción"
        self.fecha_ingreso = fecha_ingreso

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "especie": self.especie,
            "estado": self.estado,
            "fecha_ingreso": self.fecha_ingreso
        }
