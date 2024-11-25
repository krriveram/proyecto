from Deck import Deck
from Tablero import Tablero
import random


class Jugador:

    def __init__(self, nombre, deck):
        self.nombre = nombre
        self.vida = 4000
        self.deck = deck
        self.cartasMano = []
        self.tablero = Tablero()

    def crearMano(self, cartas):
        ManoCartas=[]
        for k in range(5):
            posicionAleatoria=random.randint(1,len(cartas)-1)
            mano=cartas[posicionAleatoria]
            ManoCartas.append(mano)
        return ManoCartas
    
    def robarCartaDeck(self,deck,ManoCartas):
        self.deck=deck
        self.ManoCartas=ManoCartas
        cartaRobada=deck.robarCarta()
        ManoCartas.append(cartaRobada)


    def mons_en_tablero(self, carta, posicion, modo):
        self.tablero.colocar_monstruo(carta, posicion, modo)
        self.cartasMano.remove(carta)

    def magtram_en_tablero(self, carta, posicion, modo):
        self.tablero.colocar_magica_trampa(carta, posicion)
        self.cartasMano.remove(carta)