from Tablero import Tablero
from Jugador import Jugador
from Deck import Deck
from CartaYuGiOh import Monstruo, Magica, Trampa
from enum import Enum
import random as rd

class Turno(Enum):
    JUGADOR = 1
    MAQUINA = 2

class Juego:
    def __init__(self, jugador, maquina):
        self.jugador = jugador
        self.maquina = maquina
        self.tablero = {
            "magicas_trampas_maquina": [None, None, None],
            "monstruos_maquina": [None, None, None],
            "monstruos_jugador": [None, None, None],
            "magicas_trampas_jugador": [None, None, None]
        }
        self.turno_actual = Turno(rd.choice([1, 2]))
        self.turno = 1

    def actualizar_tablero(self):
        self.mostrar_tablero()

    def mostrar_tablero(self):
        print("\n=== Tablero ===")
        print(f"Vida del Jugador: {self.jugador.vida} | Vida de la Máquina: {self.maquina.vida}\n")
        
        print("Máquina: ")
        print("Cartas Mágicas/Trampa:")
        for carta in self.tablero["magicas_trampas_maquina"]:
            print(f"[ {carta.nombre if carta else '---'} ]", end=" ")
        print("\nCartas Monstruo:")
        for carta in self.tablero["monstruos_maquina"]:
            if carta:
                estado = f"ATK: {carta.ataque}" if carta.modo == "ataque" else f"DEF: {carta.defensa}"
                boca_arriba = "(Boca arriba)" if carta.boca_arriba else "(Boca abajo)"
                print(f"[ {carta.nombre} {estado} {boca_arriba} ]", end=" ")
            else:
                print("[ --- ]", end=" ")
        print("\n")

        print("Jugador: ")
        print("Cartas Mágicas/Trampa:")
        for carta in self.tablero["magicas_trampas_jugador"]:
            print(f"[ {carta.nombre if carta else '---'} ]", end=" ")
        print("\nCartas Monstruo:")
        for carta in self.tablero["monstruos_jugador"]:
            if carta:
                estado = f"ATK: {carta.ataque}" if carta.modo == "ataque" else f"DEF: {carta.defensa}"
                boca_arriba = "(Boca arriba)" if carta.boca_arriba else "(Boca abajo)"
                print(f"[ {carta.nombre} {estado} {boca_arriba} ]", end=" ")
            else:
                print("[ --- ]", end=" ")
        print("\n")
        
        print("Cartas en la Mano del Jugador:")
        for carta in self.jugador.cartasMano:
            print(f"{carta.nombre} | Tipo: {carta.tipo}", end=", ")
        print("\n=== Fin del Tablero ===\n")

    def fase_tomar_carta(self, jugador):
        if jugador.deck.cartas:
            carta_robada = jugador.deck.robarCarta()
            jugador.cartasMano.append(carta_robada)
            print(f"{jugador.nombre} ha robado una carta: {carta_robada.nombre}")
        else:
            print(f"El mazo de {jugador.nombre} está vacío. No puede robar más cartas.")
      
    def fase_principal(self, jugador):
        while True:
            self.mostrar_tablero()
            print(f'Opciones:\n1. Jugar una carta en mano.\n2. Cambiar el modo de una carta en juego.\n3. Declarar batalla.')
            numero = int(input('Ingrese la opción que quiera realizar: '))
            if numero == 1:
                self.jugar_carta(jugador)
                self.actualizar_tablero()
            elif numero == 2:
                self.cambiar_modo(jugador)
                self.actualizar_tablero()
            elif numero == 3:
                break
            else:
                print(f'Opción no válida, volver a escribir la opción')

    def jugar_carta(self, jugador):
        print(f'Seleccione cuál carta quiere poner en juego:')
        for indice, carta in enumerate(jugador.cartasMano):
            print(f'{indice + 1}. {carta.nombre} ({carta.tipo})')
        indice_carta = int(input("Número de carta: ")) - 1

        if 0 <= indice_carta < len(jugador.cartasMano):
            carta = jugador.cartasMano.pop(indice_carta)
            if carta.tipo == "Monstruo":
                # Colocar carta de monstruo
                print(f'¿Cómo desea colocar la carta?\n1. Modo Ataque\n2. Modo Defensa')
                modo = int(input("Selecciona el modo: "))
                if modo == 1:
                    carta.modo = "ataque"
                    carta.boca_arriba = True
                elif modo == 2:
                    carta.modo = "defensa"
                    carta.boca_arriba = False
                else:
                    print("Modo no válido. Carta devuelta a la mano.")
                    jugador.cartasMano.append(carta)
                    return

                print("Escriba el espacio para colocar el monstruo (respuesta entre el 1 al 3):")
                posicion = int(input("Posición: ")) - 1
                if 0 <= posicion <= 2 and not self.tablero["monstruos_jugador"][posicion]:
                    self.tablero["monstruos_jugador"][posicion] = carta
                else:
                    print("El espacio no es válido o ya está ocupado. Se devolverá la carta a la mano.")
                    jugador.cartasMano.append(carta)
            elif carta.tipo in ["Mágica", "Trampa"]:
                print("Escriba el espacio para colocar la carta mágica o trampa (respuesta entre el 1 al 3):")
                posicion = int(input("Posición: ")) - 1
                if 0 <= posicion <= 2 and not self.tablero["magicas_trampas_jugador"][posicion]:
                    self.tablero["magicas_trampas_jugador"][posicion] = carta
                else:
                    print("El espacio no es válido o ya está ocupado. Se devolverá la carta a la mano.")
                    jugador.cartasMano.append(carta)
            else:
                print("No puedes jugar este tipo de carta.")
                jugador.cartasMano.append(carta)
        else:
            print("Selección no válida.")

    def cambiar_modo(self, jugador):
        print("Seleccione cuál carta desea cambiar de modo (solo cartas boca arriba):")
        monstruos = self.tablero["monstruos_jugador"] if jugador == self.jugador else self.tablero["monstruos_maquina"]
        cartas_disponibles = [(i, carta) for i, carta in enumerate(monstruos) if carta and carta.boca_arriba]
        
        if not cartas_disponibles:
            print("No hay cartas disponibles para cambiar de modo.")
            return
        
        for i, (indice, carta) in enumerate(cartas_disponibles):
            print(f'{i + 1}. {carta.nombre} (Modo: {carta.modo})')

        seleccion = int(input("Número de carta a cambiar de modo: ")) - 1

        if 0 <= seleccion < len(cartas_disponibles):
            indice, carta = cartas_disponibles[seleccion]
            carta.modo = "defensa" if carta.modo == "ataque" else "ataque"
            print(f"{carta.nombre} ha cambiado su modo a {carta.modo}.")
        else:
            print("Selección inválida.")

    def accion_maquina(self):
        print("\n=== Turno de la Máquina ===")
        self.fase_tomar_carta(self.maquina)

        for carta in self.maquina.cartasMano:
            if isinstance(carta, (Magica, Trampa)):
                espacio = self.buscar_espacio_libre(self.tablero["magicas_trampas_maquina"])
                if espacio is not None:
                    self.tablero["magicas_trampas_maquina"][espacio] = carta
                    self.maquina.cartasMano.remove(carta)
                    print(f"La máquina ha colocado la carta mágica/trampa: {carta.nombre}")
                    self.actualizar_tablero()
        
        for carta in self.maquina.cartasMano:
            if isinstance(carta, Monstruo):
                espacio = self.buscar_espacio_libre(self.tablero["monstruos_maquina"])
                if espacio is not None:
                    carta.modo = "ataque" if carta.ataque > carta.defensa else "defensa"
                    carta.boca_arriba = True if carta.modo == "ataque" else False
                    self.tablero["monstruos_maquina"][espacio] = carta
                    self.maquina.cartasMano.remove(carta)
                    print(f"La máquina ha colocado el monstruo: {carta.nombre} en modo {carta.modo}.")
                    self.actualizar_tablero()
                    break
        
        self.fase_batalla(self.maquina)
    
    def fase_batalla(self, atacante):
        print(f"\n=== Fase de Batalla de {atacante.nombre} ===")
        if atacante == self.jugador:
            atacantes = self.tablero["monstruos_jugador"]
            defensores = self.tablero["monstruos_maquina"]
        else:
            atacantes = self.tablero["monstruos_maquina"]
            defensores = self.tablero["monstruos_jugador"]

        for atacante in atacantes:
            if atacante and atacante.modo == "ataque":
                if not any(defensores):
                    oponente = self.maquina if atacante == self.jugador else self.jugador
                    oponente.vida -= atacante.ataque
                    print(f"{atacante.nombre} realiza un ataque directo. {oponente.nombre} pierde {atacante.ataque} puntos de vida.")
                    if oponente.vida <= 0:
                        print(f"{oponente.nombre} ha sido derrotado.")
                        return
                else:
                    defensores_disponibles = [d for d in defensores if d is not None]
                    defensor = rd.choice(defensores_disponibles)
                    print(f"{atacante.nombre} ataca a {defensor.nombre}.")
                    if atacante.ataque > defensor.defensa:
                        print(f"{defensor.nombre} es destruido.")
                        defensores[defensores.index(defensor)] = None
                    else:
                        print(f"{atacante.nombre} no logra destruir a {defensor.nombre}.")

    def buscar_espacio_libre(self, espacios):
        for i, espacio in enumerate(espacios):
            if espacio is None:
                return i
        return None

    def iniciar_juego(self):
        print(f"\nJugador: {self.jugador.nombre} vs Máquina: {self.maquina.nombre}")
        print(f"Vida inicial: {self.jugador.vida} (Jugador), {self.maquina.vida} (Máquina)\n")
        
        for _ in range(5):
            self.fase_tomar_carta(self.jugador)
            self.fase_tomar_carta(self.maquina)

        while self.jugador.vida > 0 and self.maquina.vida > 0:
            print(f"\nTurno {self.turno}: {'Jugador' if self.turno_actual == Turno.JUGADOR else 'Máquina'}")
            self.mostrar_tablero()
            if self.turno_actual == Turno.JUGADOR:
                self.fase_tomar_carta(self.jugador)
                self.fase_principal(self.jugador)
                self.fase_batalla(self.jugador)
            else:
                self.accion_maquina()

            self.cambiar_turno()
            self.turno += 1

        ganador = self.jugador if self.jugador.vida > 0 else self.maquina
        print(f"\n¡El ganador es {ganador.nombre}!")

    def cambiar_turno(self):
        if self.turno_actual == Turno.JUGADOR:
            self.turno_actual = Turno.MAQUINA
        else:
            self.turno_actual = Turno.JUGADOR


jugador = Jugador(nombre="Jugador", vida=4000, deck=Deck.generar_deck())
maquina = Jugador(nombre="Máquina", vida=4000, deck=Deck.generar_deck())

juego = Juego(jugador, maquina)
juego.iniciar_juego()
