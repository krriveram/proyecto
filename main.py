import CartaYuGiOh
import TipoCarta
import Monstruo
import Deck

cartas = []
with open("cartas.txt", 'r') as file:
    for linea in file:
        datos = linea.strip("\n").split('/')
        nombre=datos[1]
        descripcion=datos[2]
        tipoCarta=datos[5]
        ataque=datos[6]
        defensa=datos[7]
        if  tipoCarta=="MONSTRUO":
            tipoAtributo=datos[3]
            tipoMonstruo=datos[4]
            #cartGenerada=Monstruo(nombre,descripcion,tipoCarta,ataque,defensa,tipoAtributo,tipoMonstruo)
            #cartas.append(cartaGenerada)
        else:
            cartaGenerada=CartaYuGiOh(nombre,descripcion,tipoCarta,ataque,defensa)
            cartas.append(cartaGenerada)

Mideck= Deck(cartas)
print(Mideck)
#JUEGO
