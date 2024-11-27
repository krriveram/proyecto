class CartaYuGiOh:
    
    def __init__(self, tipo, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
    def __repr__(self):
        return f"{self.tipo}: {self.nombre} - {self.descripcion}"
        