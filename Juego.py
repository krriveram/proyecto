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
        self.incrementos_temporales = {
            "monstruos_maquina": [0, 0, 0],
            "monstruos_jugador": [0, 0, 0]
        }

    def mostrar_tablero(self):
        print("\n=== Tablero ===")
        print(f"Vida del Jugador: {self.jugador.vida} | Vida del BOT: {self.maquina.vida}\n")

        self.mostrar_cartas("BOT - Cartas Mágicas/Trampa:", self.tablero["magicas_trampas_maquina"])
        self.mostrar_cartas("BOT - Cartas Monstruo:", self.tablero["monstruos_maquina"], mostrar_detalles=True)

        self.mostrar_cartas("Jugador - Cartas Monstruo:", self.tablero["monstruos_jugador"], mostrar_detalles=True)
        self.mostrar_cartas("Jugador - Cartas Mágicas/Trampa:", self.tablero["magicas_trampas_jugador"])

        print("\nCartas en la Mano del Jugador:")
        for carta in self.jugador.cartasMano:
            if isinstance(carta, Monstruo):
                print(f"Monstruo: {carta.nombre} | Atributo: {carta.atributo} | Tipo: {carta.tipo_monstruo} | "
                      f"ATK: {carta.ataque} | DEF: {carta.defensa} | Boca arriba: {'sí' if carta.boca_arriba else 'no'} | Modo: {carta.modo}")
            elif isinstance(carta, Magica):
                print(f"Mágica: {carta.nombre} | Tipo: {carta.tipo_objetivo} | Incremento: {carta.incremento}")
            elif isinstance(carta, Trampa):
                print(f"Trampa: {carta.nombre} | Tipo: {carta.tipo_objetivo}")

        print("\n=== Fin del Tablero ===\n")

    def mostrar_cartas(self, titulo, cartas, mostrar_detalles=False):
        print(titulo)
        for carta in cartas:
            if carta is None:
                print("[ VACÍO ]", end=" ")
            else:
                if isinstance(carta, Monstruo):
                    if carta.boca_arriba:
                        if mostrar_detalles:
                            print(f"[ {self.mostrar_detalles_monstruo(carta)} ]", end=" ")
                        else:
                            print(f"[ {carta.nombre} ]", end=" ")
                    else:
                        print("[ Carta Boca Abajo ]", end=" ")
                else:
                    print(f"[ {carta.nombre} ]", end=" ")
        print("\n")


    def mostrar_detalles_monstruo(self, carta):
        return (f'Monstruo: {carta.nombre} | Atributo: {carta.atributo} | Tipo: {carta.tipo_monstruo} | '
                f'ATK: {carta.ataque} | DEF: {carta.defensa} | '
                f'Boca arriba: {"sí" if carta.boca_arriba else "no"} | Modo: {carta.modo}')

    def fase_tomar_carta(self, jugador):
        if jugador.deck.cartas:
            carta_robada = jugador.deck.robarCarta()
            jugador.cartasMano.append(carta_robada)
            if jugador == self.jugador:
                print(f"{jugador.nombre} ha robado una carta: {carta_robada.nombre}")
        else:
            print(f"El mazo de {jugador.nombre} está vacío. No puede robar más cartas.")

    def fase_principal(self, jugador):
        validacion = input(str('Desea pasar su turno? (si o no): ')).upper()
        while validacion=="NO":
            print("\n=== Fase Principal ===")
            self.mostrar_tablero()
            
            opciones = [
                "1. Jugar una carta en mano.",
                "2. Cambiar el modo de una carta en juego.",
            ]
            if self.turno > 1:
                if self.turno_actual == Turno.JUGADOR:
                    opciones.append("3. Declarar batalla.")
                    opciones.append("4. Terminar fase principal.")
                else:
                    opciones.append("3. Terminar fase principal.")
            else:
                opciones.append("3. Terminar fase principal.")

            for opcion in opciones:
                print(opcion)
                
            opcion_seleccionada = int(input('Ingrese la opción que quiera realizar: '))
            
            while(opcion_seleccionada<1 and opcion_seleccionada>4):
                opcion_seleccionada = int(input('Ingrese una opci[on del 1 al 4: '))

            if opcion_seleccionada == 1:
                self.jugar_carta(jugador)
            elif opcion_seleccionada == 2:
                self.cambiar_modo(jugador)
            elif opcion_seleccionada == 3 and self.turno > 1 and self.turno_actual == Turno.JUGADOR:
                self.declarar_batalla_usuario()
                break
            elif opcion_seleccionada == 3 or (opcion_seleccionada == 4 and self.turno_actual == Turno.JUGADOR):
                break

                
    def jugar_carta(self, jugador):
        continuar_jugando = "si"

        while continuar_jugando.lower() == "si":
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
            elif isinstance(carta, (Magica, Trampa)):
                espacio = int(input("Escriba el espacio para colocar la carta mágica o trampa (respuesta entre el 1 al 3): ")) - 1
                if espacio < 0 or espacio >= len(self.tablero["magicas_trampas_jugador"]) or self.tablero["magicas_trampas_jugador"][espacio] is not None:
                    print("Espacio no válido o ocupado.")
                    continue

                self.tablero["magicas_trampas_jugador"][espacio] = carta
                jugador.cartasMano.pop(num_carta)
                print(f"Has colocado la carta {'Mágica' if isinstance(carta, Magica) else 'Trampa'}: {carta.nombre}")
                print(f"Descripción: {carta.descripcion}")

            continuar_jugando = input("¿Quieres poner otra carta en juego? (sí/no): ")


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
    
    def aplicar_incremento_magico_temporal(self, campo_magicas_trampas, campo_monstruos):
        for i, magia in enumerate(self.tablero[campo_magicas_trampas]):
            if isinstance(magia, Magica):
                for j, monstruo in enumerate(self.tablero[campo_monstruos]):
                    if monstruo is not None and monstruo.tipo_monstruo == magia.tipo_objetivo:
                        incremento_anterior = monstruo.ataque
                        incremento = magia.incremento
                        monstruo.ataque += incremento
                        self.incrementos_temporales[campo_monstruos][j] += incremento
                        print(f"La carta {monstruo.nombre} recibe un incremento de ataque de {incremento} "
                            f"debido a la carta mágica {magia.nombre}. Nuevo ATK: {monstruo.ataque} (anterior: {incremento_anterior})")

    def remover_incremento_magico_temporal(self, campo_monstruos):
        for i, incremento in enumerate(self.incrementos_temporales[campo_monstruos]):
            if incremento > 0 and self.tablero[campo_monstruos][i] is not None:
                monstruo = self.tablero[campo_monstruos][i]
                monstruo.ataque -= incremento
                print(f"El incremento temporal de ataque de {incremento} puntos aplicado a {monstruo.nombre} se ha eliminado. "
                    f"Nuevo ATK: {monstruo.ataque}")
            self.incrementos_temporales[campo_monstruos][i] = 0


    def declarar_batalla_usuario(self):
        print("\n=== Fase de Batalla de Jugador ===")

        atacantes = [carta for carta in self.tablero["monstruos_jugador"] if carta and carta.modo == "ataque"]
        if not atacantes:
            print("No hay monstruos en modo ataque para atacar.")
            return

        defensores_disponibles = [carta for carta in self.tablero["monstruos_maquina"] if carta]
        for atacante in atacantes:
            if not defensores_disponibles:
                print(f"{atacante.nombre} realiza un ataque directo. BOT pierde {atacante.ataque} puntos de vida.")
                self.maquina.vida -= atacante.ataque
                if self.maquina.vida <= 0:
                    print("¡BOT ha sido derrotado!")
                    return
            else:
                print("\nElige el objetivo a atacar:")
                for index, defensor in enumerate(defensores_disponibles):
                    print(f"{index + 1}. {self.mostrar_detalles_monstruo(defensor)}")

                objetivo = -1
                while objetivo < 0 or objetivo >= len(defensores_disponibles):
                    seleccion = input(f"Selecciona el número del objetivo para que {atacante.nombre} ataque: ")

                    if seleccion.isdigit():
                        objetivo = int(seleccion) - 1
                        if objetivo < 0 or objetivo >= len(defensores_disponibles):
                            print("Error: Número de objetivo no válido. Inténtelo de nuevo.")
                    else:
                        print("Error: Debe ingresar un número válido.")
                        objetivo = -1

                defensor = defensores_disponibles[objetivo]
                self.resolver_ataque(atacante, defensor, "monstruos_maquina")

                defensores_disponibles = [carta for carta in self.tablero["monstruos_maquina"] if carta]



    def declarar_batalla_maquina(self):
        print("\n=== Fase de Batalla de BOT ===")
        atacantes = [carta for carta in self.tablero["monstruos_maquina"] if carta and carta.modo == "ataque"]
        defensores = [carta for carta in self.tablero["monstruos_jugador"] if carta]
        if not atacantes:
            print("El BOT no tiene monstruos en modo ataque para realizar una batalla.")
            return

        for atacante in atacantes:
            defensores = [carta for carta in self.tablero["monstruos_jugador"] if carta]
            if defensores:
                defensor = min(defensores, key=lambda x: x.ataque if x.modo == "ataque" else x.defensa)
                self.resolver_ataque(atacante, defensor, "monstruos_jugador")
            else:
                print(f"{atacante.nombre} realiza un ataque directo. Jugador pierde {atacante.ataque} puntos de vida.")
                self.jugador.vida -= atacante.ataque
                if self.jugador.vida <= 0:
                    print("¡Jugador ha sido derrotado!")
                    return

    def resolver_ataque(self, carta_atacante, defensor, campo_defensores):
        trampa_clave = f"magicas_trampas_{'jugador' if campo_defensores == 'monstruos_jugador' else 'maquina'}"
        for i, trampa in enumerate(self.tablero[trampa_clave]):
            if isinstance(trampa, Trampa) and trampa.tipo_objetivo == carta_atacante.atributo:
                print(f"¡Se activa la trampa {trampa.nombre}! El ataque de {carta_atacante.nombre} es detenido.")
                self.tablero[trampa_clave][i] = None
                return

        print(f"{carta_atacante.nombre} ataca a {defensor.nombre}.")
        if defensor.modo == "ataque":
            if carta_atacante.ataque > defensor.ataque:
                print(f"{defensor.nombre} es destruido. El oponente pierde {carta_atacante.ataque - defensor.ataque} puntos de vida.")
                self.tablero[campo_defensores][self.obtener_indice_monstruo(defensor, campo_defensores)] = None
                if campo_defensores == "monstruos_jugador":
                    self.jugador.vida -= carta_atacante.ataque - defensor.ataque
                else:
                    self.maquina.vida -= carta_atacante.ataque - defensor.ataque
            elif carta_atacante.ataque < defensor.ataque:
                print(f"{carta_atacante.nombre} es destruido. El atacante pierde {defensor.ataque - carta_atacante.ataque} puntos de vida.")
                atacante_campo = "monstruos_jugador" if campo_defensores == "monstruos_maquina" else "monstruos_maquina"
                self.tablero[atacante_campo][self.obtener_indice_monstruo(carta_atacante, atacante_campo)] = None
                if campo_defensores == "monstruos_jugador":
                    self.jugador.vida -= defensor.ataque - carta_atacante.ataque
                else:
                    self.maquina.vida -= defensor.ataque - carta_atacante.ataque
            else:
                print(f"Ambas cartas ({carta_atacante.nombre} y {defensor.nombre}) son destruidas.")
                self.tablero[campo_defensores][self.obtener_indice_monstruo(defensor, campo_defensores)] = None
                atacante_campo = "monstruos_jugador" if campo_defensores == "monstruos_maquina" else "monstruos_maquina"
                self.tablero[atacante_campo][self.obtener_indice_monstruo(carta_atacante, atacante_campo)] = None
        else:
            if carta_atacante.ataque > defensor.defensa:
                print(f"{defensor.nombre} es destruido.")
                self.tablero[campo_defensores][self.obtener_indice_monstruo(defensor, campo_defensores)] = None
            elif carta_atacante.ataque < defensor.defensa:
                print(f"El ataque de {carta_atacante.nombre} falla contra {defensor.nombre}. No hay cambios.")



    def iniciar_juego(self):
        print(f"\n{self.jugador.nombre} vs BOT")
        
        for _ in range(5):
            self.fase_tomar_carta(self.jugador)
            self.fase_tomar_carta(self.maquina)

        while self.jugador.vida > 0 and self.maquina.vida > 0:
            print(f"\nTurno {self.turno}: {'Jugador' if self.turno_actual == Turno.JUGADOR else 'BOT'}")
            self.mostrar_tablero()

            if self.turno_actual == Turno.JUGADOR:
                self.fase_tomar_carta(self.jugador)
                self.aplicar_incremento_magico_temporal("magicas_trampas_jugador", "monstruos_jugador")
                self.fase_principal(self.jugador)
            else:
                self.fase_tomar_carta(self.maquina)
                self.aplicar_incremento_magico_temporal("magicas_trampas_maquina", "monstruos_maquina")
                self.accion_maquina()
                
            self.remover_incremento_magico_temporal("monstruos_maquina")
            self.cambiar_turno()
            self.turno += 1

        ganador = self.jugador if self.jugador.vida > 0 else self.maquina
        print(f"\n¡El ganador es {ganador.nombre}!")

    def obtener_indice_monstruo(self, carta, campo):
        for i, monstruo in enumerate(self.tablero[campo]):
            if monstruo == carta:
                return i
        return None


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

        self.aplicar_incremento_magico_temporal("magicas_trampas_maquina", "monstruos_maquina")

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
            self.declarar_batalla_maquina()

        self.remover_incremento_magico_temporal("monstruos_maquina")

    def buscar_espacio_libre(self, espacios):
        for indice, espacio in enumerate(espacios):
            if espacio is None:
                return indice
        return None
    
    def cambiar_turno(self):
        self.turno_actual = Turno.MAQUINA if self.turno_actual == Turno.JUGADOR else Turno.JUGADOR
        

jugador = Jugador(nombre="Jugador", vida=4000, deck=Deck.generar_deck())
maquina = Jugador(nombre="BOT", vida=4000, deck=Deck.generar_deck())

juego = Juego(jugador, maquina)
juego.iniciar_juego()
