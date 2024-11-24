from tablero import Tablero
from jugador import Jugador
from deck import Deck
from carta import CartaYuGiOh, Monstruo, Magica, Trampa
from enum import Enum

class Turno(Enum):
  JUGADOR = 1
  MAQUINA = 2

class Juego:
  def __init__(self, jugador, maquina):
    self.jugador = jugador
    self.maquina = maquina
    self.tablero = Tablero()
    


