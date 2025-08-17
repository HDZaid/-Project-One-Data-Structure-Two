class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        self.ID = None
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Proveedor: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"
    
    def __eq__(self, other):
        if isinstance(other, Proveedor):
            return self.nombre == other.nombre and self.direccion == other.direccion and self.telefono == other.telefono
        return False