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
    self.turno = 1
    self.turno_actual = Turno.JUGADOR
  
  def fase_tomar_carta(self, jugador):
    print('f El jugador: {jugador.nombre} decide robar una carta')
    if not carta:
      print(f'No hay mas cartas en el Deck')

  def fase_principal(self, jugador):
    while True:
      self.mostrar_tablero()
      self.mostrar_mano(jugador)
      print(f'Opciones:
      1. Jugar una carta en mano.
      2. Cambiar el modo de una carta en juego.
      3. Declarar batalla.')
      numero = int(input('Ingrese la opcion que quiera realizar: '))
      if numero == 1:
        self.jugar_carta(jugador)
      elif numero == 2:
        self.cambiar_modo(jugador)
      elif numero == 3:
        break
      else:
        print(f'Opcion no valida, volver a escribir la opcion')
    
  def jugar_carta(self, jugador):
    print(f'Seleccione cual carta quiere poner en juego')
    for indice, carta in enumerate(jugador.mano):
      print(f'{indice + 1}. {carta}')
          indice_carta = int(input("Número de carta: ")) - 1
      
      if 0 <= indice_carta < len(jugador.mano):
        carta = jugador.mano.pop(seleccion)
        if carta.tipo == "Monstruo":
            print(f'¿Cómo desea colocar la carta?
            1. Modo Ataque
            2. Modo Defensa')
            modo = int(input("Selecciona el modo: ")
            if modo == 1:
                carta.modo = "ataque"
                carta.boca_arriba = True
                print(f"{jugador.nombre} ha colocado {carta.nombre} en modo Ataque (boca arriba).")
            elif modo == 2:
                carta.modo = "defensa"
                carta.boca_arriba = False
                print(f"{jugador.nombre} ha colocado {carta.nombre} en modo Defensa (boca abajo).")
            else:
                print("Modo no válido. Carta devuelta a la mano.")
                jugador.mano.append(carta)
                return
              
            print("Escriba el espacio para colocar el monstruo respuesta entre el 1 al 3:")
            posicion = int(input("Posición: ")) - 1
            if 0 <= posicion <= 2 and not self.tablero.jugador["monstruos"][posicion]:
                self.tablero.jugador["monstruos"][posicion] = carta
                print(f"{jugador.nombre} ha colocado {carta.nombre} en el tablero.")
            else:
                print("El espacio no es válido o ya está ocupado. Se devolverá la carta a la mano.")
                jugador.mano.append(carta)
        elif carta.tipo in ["Mágica", "Trampa"]:
            print("Escriba el espacio para colocar la carta mágica o trampa respuesta entre el 1 al 3:")
            posicion = int(input("Posición: ")) - 1
            if 0 <= posicion <= 2 and not self.tablero.jugador["magicas_trampas"][posicion]:
                self.tablero.jugador["magicas_trampas"][posicion] = carta
                print(f"{jugador.nombre} ha colocado {carta.nombre} en el tablero.")
            else:
                print("El espacio no es válido o ya está ocupado. Se devolverá la carta a la mano.")
                jugador.mano.append(carta)
        else:
            print("No puedes jugar este tipo de carta.")
            jugador.mano.append(carta)
      else:
        print("Selección no válida.")

  def cambiar_turno(self):
    if self.turno_actual == Turno.JUGADOR:
    self.turno_actual = Turno.MAQUINA
else:
    self.turno_actual = Turno.JUGADOR

  def fase_batalla(self):
    print('me canse luego sigo xd')
  
  def iniciar_juego(self):
    print(f'Estamos en el turno {self.turno} y le toca a {self.turno_actual.name}')
    if self.turno_actual == Turno.JUGADOR:
      self.fase_tomar_carta(self.jugador)
      self.fase_principal(self.jugador)
    else:
      self.fase_tomar_carta(self.maquina)
      self.fase_principal(self.maquina)
    self.fase_batalla
    self.cambiar_turno()
    self.turno += 1
    


