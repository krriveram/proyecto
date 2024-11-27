class Jugador:
    def __init__(self, nombre, vida, deck):
        self.nombre = nombre
        self.vida = vida
        self.deck = deck
        self.cartasMano = []

    def robar_carta(self):
        if self.deck.cartas:
            return self.deck.robarCarta()
        else:
            return None

    def jugar_carta(self, indice):
        if 0 <= indice < len(self.cartasMano):
            return self.cartasMano.pop(indice)
        else:
            print("Error: índice fuera de rango.")
            return None
