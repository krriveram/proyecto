from Deck import Deck
from Tablero import Tablero
import random


class Jugador:

    deck=Deck('cartas.txt')

    def __init__(self, nombre, deck):
        self.nombre = nombre
        self.vida = 4000
        self.deck = deck
        self.cartasMano = []
        self.tablero = Tablero()

    def crearMano(self, archivo):
        ManoCartas=[]
        with open(archivo, 'r') as Mano:
            for linea in Mano:
                posicionAleatoria=random.randint(1,28)
                carta=linea.strip('\n').split('/')[posicionAleatoria]
                while len(ManoCartas)<5:
                    ManoCartas.append(carta)
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