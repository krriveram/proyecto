from CartaYuGiOh import CartaYuGiOh, TipoCarta

class Trampa(CartaYuGiOh):
    def __init__(self, nombre, descripcion, atributo_detenido):
        super().__init__(nombre, descripcion, TipoCarta.TRAMPA)
        self.atributo_detenido = atributo_detenido

    def posible_detener(self, carta_atacando):
        return carta_atacando.atributo == self.atributo_detenido

    def activar_detener(self, carta):
        if self.posible_detener(carta):
            return True  # El ataque es bloqueado
        return False