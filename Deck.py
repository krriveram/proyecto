import random
from CartaYuGiOh import CartaYuGiOh
import TipoCarta
class Deck:
    
    def __init__(self, cartasDeck, archivo):
        cartasDeck=[]
        contMon=0
        contTram=-0
        contMag=0
        with open(archivo, 'r') as deckCartas:
            for linea in deckCartas:
                posicionAleatoria=random.randint(1,28)
                carta=linea.strip('\n').split('/')[posicionAleatoria]
                while contMon<20 or contTram<5 or contMag<5:
                    if carta[5]==TipoCarta.MONSTRUO.value:
                        cartasDeck.add(carta)
                        contMon+=1
                    elif carta[5]==TipoCarta.TRAMPA.value:
                       cartasDeck.add(carta)
                       contTram+=1
                    elif carta[5]==TipoCarta.MAGICA.value:
                        cartasDeck.add(carta)
                        contMag+=1
        self.cartasDeck = cartasDeck    

    def robar_carta(self):
        if self.cartasDeck:
            cartAle=random.randint(1,49)
            return self.cartasDeck.pop(cartAle)
        return None