class Proveedor:
    def __init__(self, nombre, id, servicio, calificacion):
        self.nombre = nombre
        self.id = id
        self.servicio = servicio
        self.calificacion = calificacion

    def __str__(self):
        return (
            '=' * 50 +
            f"\n ID: {self.id} \n Proveedor: {self.nombre}\n Tipo de Servicio: {self.servicio} \n Calificación: {self.enmascarado_calificacion()}\n" +
            '=' * 50 + "\n"
        )

    def enmascarado_calificacion(self):
        return '★ ' * int(self.calificacion)
    
    def __eq__(self, other):
        if isinstance(other, Proveedor):
            return (self.nombre == other.nombre and 
                    self.id == other.id and 
                    self.servicio == other.servicio and 
                    self.calificacion == other.calificacion)
        elif isinstance(other, str):
            return self.servicio == other
        elif isinstance(other, int):
            return self.id == other
        return False

    def __lt__(self, other):
        if isinstance(other, Proveedor):
            return self.id < other.id
        elif isinstance(other, int):
            return self.calificacion < other
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Proveedor):
            return self.id > other.id
        elif isinstance(other, int):
            return self.calificacion > other
        return NotImplemented
        