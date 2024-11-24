from CartaYuGiOh import CartaYuGiOh, TipoCarta

class Magicas(CartaYuGiOh):
    def __init__(self, nombre, descripcion, tipo_monstruo, buff):
        super().__init__(nombre, descripcion, TipoCarta.MAGICA)
        self.tipo_monstruo = tipo_monstruo
        self.buff = buff

    def posible_buff(self, carta_jugando):
        return carta_jugando.tipo_monstruo == self.tipo_monstruo

    def activar_buff(self, carta_jugando):
        if self.posible_buff(carta_jugando):
            if "ataque" in self.descripcion.lower():
                carta_jugando.ataque += self.buff
            elif "defensa" in self.descripcion.lower():
                carta_jugando.defensa += self.buff