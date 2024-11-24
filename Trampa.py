from CartaYuGiOh import CartaYuGiOh, TipoCarta

class Trampa(CartaYuGiOh):
class CartaTrampa(Carta):
    def __init__(self, carta_id, nombre, descripcion, atributo_objetivo):
        super().__init__(carta_id, nombre, descripcion, TipoCarta.TRAMPA)
        self.atributo_objetivo = atributo_objetivo

    def __str__(self):
        return (f"{super().__str__() \nAtributo: {self.atributo_objetivo}")

    def posible_detener(self, carta_atacando):
        return carta_atacando.atributo == self.atributo_detenido
