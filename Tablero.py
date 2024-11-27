class Tablero:
    def __init__(self):
        self.espacio_monstruo_jugador = [None, None, None]
        self.espacio_magtramp_jugador = [None, None, None]
        self.espacio_monstruo_maquina = [None, None, None]
        self.espacio_magtramp_maquina = [None, None, None]

    def colocar_monstruo(self, jugador, indice, carta):
        if jugador == "jugador":
            if self.espacio_monstruo_jugador[indice] is None:
                self.espacio_monstruo_jugador[indice] = carta
                print(f"{carta.nombre} colocado en el espacio {indice + 1} del jugador.")
            else:
                print("El espacio está ocupado.")
        elif jugador == "maquina":
            if self.espacio_monstruo_maquina[indice] is None:
                self.espacio_monstruo_maquina[indice] = carta
                print(f"{carta.nombre} colocado en el espacio {indice + 1} de la máquina.")
            else:
                print("El espacio está ocupado.")
        else:
            print("Error: Jugador desconocido.")

    def colocar_magica_trampa(self, jugador, indice, carta):
        if jugador == "jugador":
            if self.espacio_magtramp_jugador[indice] is None:
                self.espacio_magtramp_jugador[indice] = carta
                print(f"{carta.nombre} colocado en el espacio {indice + 1} del jugador.")
            else:
                print("El espacio está ocupado.")
        elif jugador == "maquina":
            if self.espacio_magtramp_maquina[indice] is None:
                self.espacio_magtramp_maquina[indice] = carta
                print(f"{carta.nombre} colocado en el espacio {indice + 1} de la máquina.")
            else:
                print("El espacio está ocupado.")
        else:
            print("Error: Jugador desconocido.")

    def mostrar_tablero(self):
        print("\n=== Estado del Tablero ===")
        print("Monstruos del Jugador:")
        for i, carta in enumerate(self.espacio_monstruo_jugador):
            if carta:
                print(f"Espacio {i + 1}: {carta.nombre} (ATK: {carta.ataque} / DEF: {carta.defensa})")
            else:
                print(f"Espacio {i + 1}: [VACÍO]")

        print("\nCartas Mágicas/Trampas del Jugador:")
        for i, carta in enumerate(self.espacio_magtramp_jugador):
            if carta:
                print(f"Espacio {i + 1}: {carta.nombre}")
            else:
                print(f"Espacio {i + 1}: [VACÍO]")

        print("\nMonstruos de la Máquina:")
        for i, carta in enumerate(self.espacio_monstruo_maquina):
            if carta:
                print(f"Espacio {i + 1}: {carta.nombre} (ATK: {carta.ataque} / DEF: {carta.defensa})")
            else:
                print(f"Espacio {i + 1}: [VACÍO]")

        print("\nCartas Mágicas/Trampas de la Máquina:")
        for i, carta in enumerate(self.espacio_magtramp_maquina):
            if carta:
                print(f"Espacio {i + 1}: {carta.nombre}")
            else:
                print(f"Espacio {i + 1}: [VACÍO]")
        print("==========================\n")
