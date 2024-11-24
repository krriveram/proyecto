from CartaYuGiOh import CartaYuGiOh, TipoCarta

class Magicas(CartaYuGiOh):
    def __init__(self, carta_id, nombre, descripcion, incremento, tipo_objetivo):
        super().__init__(carta_id, nombre, descripcion, TipoCarta.MAGICA)
        self.incremento = incremento
        self.tipo_objetivo = tipo_objetivo

    def __str__(self):
        return (f"{super().__str__()} \n Incremento: {self.incremento}")
