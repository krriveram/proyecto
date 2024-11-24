class Tablero:
  def __init__(self):
      self.espacio_monstruo_jugador = [None] * 3
      self.espacio_magtramp_jugador = [None] * 3
      self.espacio_monstruo_maquina = [None] * 3
      self.espacio_magtramp_maquina = [None] * 3

    def colocar_carta(self, carta, espacio):
        if espacio in range(3):
            if carta.tipo_carta == 'Monstruo':
                self.espacio_monstruo_jugador[espacio] = carta
            else:
                self.espacio_magtramp_jugador[espacio] = carta
