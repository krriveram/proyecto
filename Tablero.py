class Tablero:
  def __init__(self):
      self.espacioMonstruo = [None] * 3
      self.espacioTraMag = [None] * 3

  def colocar_monstruo(self, carta, posicion, modo):
      if 0 <= posicion < 3:
          self.espacioMonstruo[posicion] = carta
          carta.cambiar_modo() if modo == 'defensa' else carta.colocar_en_ataque()

  def colocar_magica_trampa(self, carta, posicion):
      if 0 <= posicion < 3:
          self.espacioTraMag[posicion] = carta