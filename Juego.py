from Tablero import Tablero
from Jugador import Jugador
from Deck import Deck
from CartaYuGiOh import CartaYuGiOh, Monstruo, Magica, Trampa
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
    if len(Deck)=0:
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
        carta = jugador.mano.pop(indice_carta)
        if carta.tipo == "Monstruo":
            print(f'¿Cómo desea colocar la carta?
            1. Modo Ataque
            2. Modo Defensa')
            modo = int(input("Selecciona el modo: "))
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
  
    def fase_batalla(self, atacante):
        if atacante == self.maquina:
            defensor = self.jugador 
        else:
            self.maquina
            
        print(f"{atacante.nombre} paso a la fase de batalla.")
  
        self.mostrar_tablero()
        
        if atacante == self.jugador:
            espacios_tablero = self.tablero.espacios_jugador
        else:
            espacios_tablero = self.tablero.espacios_maquina
  
        monstruos_atacantes = []
  
        for indice, carta in enumerate(espacios_tablero):
            if carta is not None:
                if isinstance(carta, Monstruo):
                    if carta.modo == "ataque":
                        if carta.boca_arriba:
                            monstruos_atacantes.append((indice, carta))
        if len(monstruos_atacantes) == 0:
            print(f"{atacante.nombre} no tiene monstruos en modo ataque para declarar batalla.")
            return
  
        for indice_atacante, carta_atacante in monstruos_atacantes:
            print(f"{atacante.nombre} ataca con {carta_atacante.nombre} (ATK: {carta_atacante.ataque})")
            
            monstruos_defensores = []
  
            for indice, carta in enumerate(espacios_tablero):
                if carta is not None:
                    if isinstance(carta, Monstruo):
                        if carta.modo == "ataque":
                            if carta.boca_arriba:
                                monstruos_defensores.append((indice, carta))
            if len(monstruos_defensores) == 0:
                print(f"{defensor.nombre} no tiene monstruos en el tablero. Ataque directo.")
                defensor.vida -= carta_atacante.ataque
                print(f"{defensor.nombre} pierde {carta_atacante.ataque} puntos de vida. Vida restante: {defensor.vida}")
                if defensor.vida <= 0:
                    print(f"{defensor.nombre} ha sido derrotado.")
                    return
                continue
  
            print("Selecciona un objetivo para el ataque:")
            for i, (indice_defensor, carta_defensora) in enumerate(monstruos_defensores):
                if not carta_defensora.boca_arriba:
                    estado = "Boca Abajo"     
                else:
                    print(f"ATK: {carta_defensora.ataque} / DEF: {carta_defensora.defensa}")
                print(f"{i + 1}. {carta_defensora.nombre} ({estado})")
  
            seleccion_defensor = int(input("Elige un objetivo para atacar: ")) - 1
            if seleccion_defensor < 0 or seleccion_defensor >= len(monstruos_defensores):
                print("Selección inválida. Se cancela el ataque.")
                continue
  
            indice_defensor, carta_defensora = monstruos_defensores[seleccion_defensor]
  
            print(f"{carta_atacante.nombre} ataca a {carta_defensora.nombre}.")
            if not carta_defensora.boca_arriba:
                carta_defensora.boca_arriba = True
                print(f"La carta {carta_defensora.nombre} se reveló.")
  
            if carta_defensora.modo == "ataque":
                if carta_atacante.ataque > carta_defensora.ataque:
                    print(f"{carta_defensora.nombre} es destruida.")
                    espacios_defensor[indice_defensor] = None
                    diferencia = carta_atacante.ataque - carta_defensora.ataque
                    defensor.vida -= diferencia
                    print(f"{defensor.nombre} pierde {diferencia} puntos de vida. Vida restante: {defensor.vida}")
                elif carta_atacante.ataque < carta_defensora.ataque:
                    print(f"{carta_atacante.nombre} es destruida.")
                    espacios_atacante[indice_atacante] = None
                    diferencia = carta_defensora.ataque - carta_atacante.ataque
                    atacante.vida -= diferencia
                    print(f"{atacante.nombre} pierde {diferencia} puntos de vida. Vida restante: {atacante.vida}")
                else:
                    print("Ambas cartas son destruidas.")
                    espacios_atacante[indice_atacante] = None
                    espacios_defensor[indice_defensor] = None
            else:
                if carta_atacante.ataque > carta_defensora.defensa:
                    print(f"{carta_defensora.nombre} es destruida.")
                    espacios_defensor[indice_defensor] = None
                else:
                    print("El ataque no tiene efecto.")
  
            if defensor.vida <= 0:
                print(f"{defensor.nombre} ha sido derrotado.")
                return
    
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
    


