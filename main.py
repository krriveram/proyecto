from CartaYuGiOh import CartaYuGiOh
from TipoCarta import TipoCarta
from Atributo import Atributo
from TipoMonstruo import TipoMonstruo
import Trampa
import Magicas
from Monstruo import Monstruo
import Deck
import random

cartas = []
with open("cartas.txt", 'r') as file:
    for linea in file:
        datos = linea.strip("\n").split('/')
        nombre=datos[1]
        descripcion=datos[2]
        tipoCarta=datos[5]
        ataque=datos[6]
        defensa=datos[7]
        if tipoCarta==TipoCarta.MONSTRUO.value:
            tipoAtributo=datos[3]
            tipoMonstruo=datos[4]
            cartGenerada=Monstruo(nombre,descripcion,tipoCarta,ataque,defensa,tipoAtributo,tipoMonstruo)
            cartas.append(cartaGenerada)
        else:
            cartaGenerada=CartaYuGiOh(nombre,descripcion,tipoCarta,ataque,defensa)
            cartas.append(cartaGenerada)