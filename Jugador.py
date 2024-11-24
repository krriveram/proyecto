from Deck import Deck
from Tablero import Tablero

class Jugador:
    def __init__(self, nombre, deck):
        self.nombre = nombre
        self.vida = 4000
        self.deck = deck
        self.cartasMano = []
        self.tablero = Tablero()

    def robar_carta(self):
        carta = self.deck.robar_carta()
        if carta:
            self.cartasMano.append(carta)

    def mons_en_tablero(self, carta, posicion, modo):
        self.tablero.colocar_monstruo(carta, posicion, modo)
        self.cartasMano.remove(carta)

    def magtram_en_tablero(self, carta, posicion, modo):
        self.tablero.colocar_magica_trampa(carta, posicion)
        self.cartasMano.remove(carta)

        '''
        holi
        '''