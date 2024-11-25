import random
class Deck:
    
    def __init__(self, cartas):
        self.cartas=cartas
        cartasDeck=[]
        contMon=0
        contTram=0
        contMag=0
        for cartita in cartas:
            while contMon<20 or contTram<5 or contMag<5:
                if cartita[5]=="MOUNSTRO":
                    cartasDeck.append(cartita)
                    contMon+=1
                elif cartita[5]=="TRAMPA":
                    cartasDeck.append(cartita)
                    contTram+=1
                elif cartita[5]=="MAGICA":
                    cartasDeck.append(cartita)
                    contMag+=1
        return cartasDeck
    
    def robarCarta(self):
        cartAle=random.randint(1,len(self))
        return self.pop(cartAle)