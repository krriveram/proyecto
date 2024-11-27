class CartaYuGiOh:
    def __init__(self, tipo, nombre, descripcion):
        self.tipo = tipo
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f"{self.tipo}: {self.nombre} - {self.descripcion}"

class Monstruo(CartaYuGiOh):
    def __init__(self, nombre, descripcion, ataque, defensa, atributo, tipo_monstruo):
        super().__init__("Monstruo", nombre, descripcion)
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.atributo = atributo
        self.tipo_monstruo = tipo_monstruo
        # Nuevos atributos para gestionar la posición en el tablero
        self.boca_arriba = False
        self.modo = "defensa"  # Por defecto se colocará en defensa boca abajo

    def __repr__(self):
        return(f"Monstruo: {self.nombre} | Atributo: {self.atributo} | Tipo: {self.tipo_monstruo} | "
               f"Ataque: {self.ataque} | Defensa: {self.defensa}")

class Magica(CartaYuGiOh):
    def __init__(self, nombre, descripcion, tipo_objetivo, incremento):
        super().__init__("Mágica", nombre, descripcion)
        self.tipo_objetivo = tipo_objetivo
        self.incremento = int(incremento)

    def __repr__(self):
        return f"Mágica: {self.nombre} | Tipo: {self.tipo_objetivo} | Incremento: {self.incremento}"

class Trampa(CartaYuGiOh):
    def __init__(self, nombre, descripcion, tipo_objetivo):
        super().__init__("Trampa", nombre, descripcion)
        self.tipo_objetivo = tipo_objetivo

    def __repr__(self):
        return f"Trampa: {self.nombre} | Tipo: {self.tipo_objetivo}"
