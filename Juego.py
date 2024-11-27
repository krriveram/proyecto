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

    def mostrar_tablero(self):
        print("\n=== Tablero ===")
        print(f"Vida del Jugador: {self.jugador.vida} | Vida del BOT: {self.maquina.vida}\n")

        print("BOT - Cartas Mágicas/Trampa:")
        for carta in self.tablero["magicas_trampas_maquina"]:
            if carta is None:
                print("[ VACÍO ]", end=" ")
            else:
                print(f"[ {carta.nombre} ]", end=" ")
        print("\n")

        print("BOT - Cartas Monstruo:")
        for carta in self.tablero["monstruos_maquina"]:
            if carta is None:
                print("[ VACÍO ]", end=" ")
            else:
                print(f"[ {self.mostrar_detalles_monstruo(carta)} ]", end=" ")
        print("\n")

        print("Jugador - Cartas Monstruo:")
        for carta in self.tablero["monstruos_jugador"]:
            if carta is None:
                print("[ VACÍO ]", end=" ")
            else:
                print(f"[ {self.mostrar_detalles_monstruo(carta)} ]", end=" ")
        print("\n")

        print("Jugador - Cartas Mágicas/Trampa:")
        for carta in self.tablero["magicas_trampas_jugador"]:
            if carta is None:
                print("[ VACÍO ]", end=" ")
            else:
                print(f"[ {carta.nombre} ]", end=" ")
        print("\n")

        print("\nCartas en la Mano del Jugador:")
        for carta in self.jugador.cartasMano:
            if isinstance(carta, Monstruo):
                print(f"Monstruo: {carta.nombre} | Atributo: {carta.atributo} | Tipo: {carta.tipo_monstruo} | ATK: {carta.ataque} | DEF: {carta.defensa} | "
                      f"Boca arriba: {'sí' if carta.boca_arriba else 'no'} | Modo: {carta.modo}")
            elif isinstance(carta, Magica):
                print(f"Mágica: {carta.nombre} | Tipo: {carta.tipo_objetivo} | Incremento: {carta.incremento}")
            elif isinstance(carta, Trampa):
                print(f"Trampa: {carta.nombre} | Tipo: {carta.tipo_objetivo}")

        print("\n=== Fin del Tablero ===\n")

    def mostrar_detalles_monstruo(self, carta):
        if carta.boca_arriba.lower()=="si":
            nombre=carta.nombre
            atributo=carta.atributo
            tipo_monstruo=carta.tipo_monstruo
            ataque=carta.ataque
            defensa=carta.defensa
            posicion="si"
            modo=carta.modo

        else:
            nombre="✠"
            atributo="✠"
            tipo_monstruo="✠"
            ataque="✠"
            defensa="✠"
            posicion="✠"
            modo="✠"

        return (f'Monstruo: {nombre} | Atributo: {atributo} | Tipo: {tipo_monstruo} | '
                f'ATK: {ataque} | DEF: {defensa} | '
                f'Boca arriba: {posicion} | Modo: {modo}')

    def fase_tomar_carta(self, jugador):
        if jugador.deck.cartas:
            carta_robada = jugador.deck.robarCarta()
            jugador.cartasMano.append(carta_robada)
            if jugador == self.jugador:
                print(f"{jugador.nombre} ha robado una carta: {carta_robada.nombre}")
        else:
            print(f"El mazo de {jugador.nombre} está vacío. No puede robar más cartas.")

    def fase_principal(self, jugador):
        continuar_fase_principal = input(str("Desea Continuar? SI, NO: ")).upper()
        while continuar_fase_principal =="SI":
            self.mostrar_tablero()
            if self.turno == 1 and self.turno_actual == Turno.JUGADOR:
                print(f'Opciones:\n1. Jugar una carta en mano.\n2. Cambiar el modo de una carta en juego.\n3. Terminar fase principal.')
            else:
                print(f'Opciones:\n1. Jugar una carta en mano.\n2. Cambiar el modo de una carta en juego.\n3. Declarar batalla.\n4. Terminar fase principal.')

                opcion_seleccionada = int(input('Incorrecto. ingrese la opción que quiera realizar: '))
            if opcion_seleccionada == 1:
                self.jugar_carta(jugador)
                self.actualizar_tablero()
            elif opcion_seleccionada == 2:
                self.cambiar_modo(jugador)
                self.actualizar_tablero()
            elif opcion_seleccionada == 3 and (self.turno > 1 or self.turno_actual == Turno.MAQUINA):
                self.fase_batalla(jugador)
            elif opcion_seleccionada == 4 or (opcion_seleccionada == 3 and self.turno == 1 and self.turno_actual == Turno.JUGADOR):
                print(f'Opción no válida, vuelva a escribir la opción.')
    def actualizar_tablero(self):
        self.mostrar_tablero()

    def aplicar_incremento_magico_a_monstruos(self, campo_magicas_trampas, campo_monstruos):
        for magia in self.tablero[campo_magicas_trampas]:
            if isinstance(magia, Magica):
                for monstruo in self.tablero[campo_monstruos]:
                    if monstruo is not None and monstruo.tipo_monstruo == magia.tipo_objetivo:
                        incremento_anterior = monstruo.ataque
                        monstruo.ataque += magia.incremento
                        print(f"La carta {monstruo.nombre} recibe un incremento de ataque de {magia.incremento} "
                              f"debido a la carta mágica {magia.nombre}. Nuevo ATK: {monstruo.ataque} (anterior: {incremento_anterior})")

    def jugar_carta(self, jugador):
        carta_jugada = False
        while not carta_jugada:
            print("Seleccione cuál carta quiere poner en juego:")
            for indice, carta in enumerate(jugador.cartasMano):
                tipo_carta = "Monstruo" if isinstance(carta, Monstruo) else ("Mágica" if isinstance(carta, Magica) else "Trampa")
                print(f"{indice + 1}. {carta.nombre} ({tipo_carta})")
            num_carta = int(input("Número de carta: ")) - 1

            if num_carta < 0 or num_carta >= len(jugador.cartasMano):
                print("Error: Carta no válida.")
                continue

            carta = jugador.cartasMano[num_carta]

            if isinstance(carta, Monstruo):
                modo = int(input("¿Cómo desea colocar la carta?\n1. Modo Ataque\n2. Modo Defensa\nSelecciona el modo: "))
                carta.modo = "ataque" if modo == 1 else "defensa"
                carta.boca_arriba = True if carta.modo == "ataque" else False

                espacio = int(input("Escriba el espacio para colocar el monstruo (respuesta entre el 1 al 3): ")) - 1
                if espacio < 0 or espacio >= len(self.tablero["monstruos_jugador"]) or self.tablero["monstruos_jugador"][espacio] is not None:
                    print("Espacio no válido o ocupado.")
                    continue

                self.tablero["monstruos_jugador"][espacio] = carta
                jugador.cartasMano.pop(num_carta)
                carta_jugada = True
            elif isinstance(carta, (Magica, Trampa)):
                espacio = int(input("Escriba el espacio para colocar la carta mágica o trampa (respuesta entre el 1 al 3): ")) - 1
                if espacio < 0 or espacio >= len(self.tablero["magicas_trampas_jugador"]) or self.tablero["magicas_trampas_jugador"][espacio] is not None:
                    print("Espacio no válido o ocupado.")
                    continue

                self.tablero["magicas_trampas_jugador"][espacio] = carta
                jugador.cartasMano.pop(num_carta)
                print(f"Has colocado la carta {'Mágica' if isinstance(carta, Magica) else 'Trampa'}: {carta.nombre}")
                print(f"Descripción: {carta.descripcion}")
                carta_jugada = True

    def cambiar_modo(self, jugador):
        campo = "monstruos_jugador" if jugador == self.jugador else "monstruos_maquina"
        print("Seleccione el monstruo cuyo modo desea cambiar:")
        for indice, carta in enumerate(self.tablero[campo]):
            if carta is not None:
                print(f"{indice + 1}. {self.mostrar_detalles_monstruo(carta)}")
        
        while True:
            num_monstruo = int(input("Número de monstruo: ")) - 1
            if num_monstruo < 0 or num_monstruo >= len(self.tablero[campo]) or self.tablero[campo][num_monstruo] is None:
                print("Error: Monstruo no válido. Intente de nuevo.")
            else:
                monstruo = self.tablero[campo][num_monstruo]
                nuevo_modo = "defensa" if monstruo.modo == "ataque" else "ataque"
                monstruo.modo = nuevo_modo
                print(f"El monstruo {monstruo.nombre} ahora está en modo {nuevo_modo}.")
                break

    def buscar_espacio_libre(self, espacios):
        for indice, espacio in enumerate(espacios):
            if espacio is None:
                return indice
        return None

    def iniciar_juego(self):
        print(f"\nJugador: {self.jugador.nombre} vs BOT")
        
        for _ in range(5):
            self.fase_tomar_carta(self.jugador)
            self.fase_tomar_carta(self.maquina)

        while self.jugador.vida > 0 and self.maquina.vida > 0:
            print(f"\nTurno {self.turno}: {'Jugador' if self.turno_actual == Turno.JUGADOR else 'BOT'}")
            self.mostrar_tablero()

            if self.turno_actual == Turno.JUGADOR:
                self.fase_tomar_carta(self.jugador)
                self.fase_principal(self.jugador)
            else:
                self.accion_maquina()

            self.cambiar_turno()
            self.turno += 1

        ganador = self.jugador if self.jugador.vida > 0 else self.maquina
        print(f"\n¡El ganador es {ganador.nombre}!")

    def cambiar_turno(self):
        self.turno_actual = Turno.MAQUINA if self.turno_actual == Turno.JUGADOR else Turno.JUGADOR

    def accion_maquina(self):
        print("\n=== Turno del BOT ===")
        self.fase_tomar_carta(self.maquina)

        for carta in self.maquina.cartasMano:
            if isinstance(carta, (Magica, Trampa)):
                espacio = self.buscar_espacio_libre(self.tablero["magicas_trampas_maquina"])
                if espacio is not None:
                    self.tablero["magicas_trampas_maquina"][espacio] = carta
                    self.maquina.cartasMano.remove(carta)
                    print(f"La máquina ha colocado la carta {'Mágica' if isinstance(carta, Magica) else 'Trampa'}: {carta.nombre}")
                    print(f"Descripción: {carta.descripcion}")

        self.aplicar_incremento_magico_a_monstruos("magicas_trampas_maquina", "monstruos_maquina")

        for carta in self.maquina.cartasMano:
            if isinstance(carta, Monstruo):
                espacio = self.buscar_espacio_libre(self.tablero["monstruos_maquina"])
                if espacio is not None:
                    carta.modo = "ataque" if carta.ataque > carta.defensa else "defensa"
                    carta.boca_arriba = True if carta.modo == "ataque" else False
                    self.tablero["monstruos_maquina"][espacio] = carta
                    self.maquina.cartasMano.remove(carta)
                    print(f"La máquina ha colocado el monstruo: {carta.nombre} en modo {carta.modo}.")

        self.mostrar_tablero()

        if self.turno > 1:
            self.fase_batalla(self.maquina)

    def fase_batalla(self, atacante):
        print(f"\n=== Fase de Batalla de {atacante.nombre} ===")
        if atacante == self.jugador:
            atacantes = self.tablero["monstruos_jugador"]
            defensores = self.tablero["monstruos_maquina"]
            oponente = self.maquina
        else:
            atacantes = self.tablero["monstruos_maquina"]
            defensores = self.tablero["monstruos_jugador"]
            oponente = self.jugador

        for carta_atacante in atacantes:
            if carta_atacante and carta_atacante.modo == "ataque":
                defensores_disponibles = [carta for carta in defensores if carta]
                if defensores_disponibles:
                    defensor = min(defensores_disponibles, key=lambda x: x.ataque if x.modo == "ataque" else x.defensa)
                    self.resolver_ataque(carta_atacante, defensor, defensores.index(defensor), defensores, atacantes, atacante, oponente)
                else:
                    print(f"{carta_atacante.nombre} realiza un ataque directo. {oponente.nombre} pierde {carta_atacante.ataque} puntos de vida.")
                    oponente.vida -= carta_atacante.ataque
                    if oponente.vida <= 0:
                        print(f"¡{oponente.nombre} ha sido derrotado!")
                        return

    def resolver_ataque(self, carta_atacante, defensor, indice_defensor, defensores, atacantes, atacante, oponente):
        trampa_clave = f"magicas_trampas_{'jugador' if oponente == self.jugador else 'maquina'}"
        for trampa in self.tablero[trampa_clave]:
            if isinstance(trampa, Trampa) and trampa.tipo_objetivo == carta_atacante.atributo:
                print(f"¡Se activa la trampa {trampa.nombre}! El ataque de {carta_atacante.nombre} es detenido.")
                return

        print(f"{carta_atacante.nombre} ataca a {defensor.nombre}.")
        if defensor.modo == "ataque":
            if carta_atacante.ataque > defensor.ataque:
                print(f"{defensor.nombre} es destruido. {oponente.nombre} pierde {abs(carta_atacante.ataque - defensor.ataque)} puntos de vida.")
                defensores[indice_defensor] = None
                oponente.vida -= abs(carta_atacante.ataque - defensor.ataque)
            elif carta_atacante.ataque < defensor.ataque:
                print(f"{carta_atacante.nombre} es destruido. {atacante.nombre} pierde {abs(defensor.ataque - carta_atacante.ataque)} puntos de vida.")
                atacantes[atacantes.index(carta_atacante)] = None
                atacante.vida -= abs(defensor.ataque - carta_atacante.ataque)
            else:
                print(f"Ambas cartas ({carta_atacante.nombre} y {defensor.nombre}) son destruidas.")
                defensores[indice_defensor] = None
                atacantes[atacantes.index(carta_atacante)] = None
        else:
            if carta_atacante.ataque > defensor.defensa:
                print(f"{defensor.nombre} es destruido.")
                defensores[indice_defensor] = None
            elif carta_atacante.ataque < defensor.defensa:
                print(f"El ataque de {carta_atacante.nombre} falla contra {defensor.nombre}. No hay cambios.")

jugador = Jugador(nombre="Jugador", vida=4000, deck=Deck.generar_deck())
maquina = Jugador(nombre="BOT", vida=4000, deck=Deck.generar_deck())

juego = Juego(jugador, maquina)
juego.iniciar_juego()