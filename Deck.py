import random
import numpy as np
from CartaYuGiOh import CartaYuGiOh

class Deck:
    def __init__(self, cartasDeck):
        self.cartasDeck = cartasDeck

    def robar_carta(self):
        if self.cartasDeck:
            return self.cartasDeck.pop(0)
        return None