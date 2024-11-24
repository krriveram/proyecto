from CartaYuGiOh import CartaYuGiOh
from TipoCarta import TipoCarta
from Atributo import Atributo
from TipoMonstruo import TipoMonstruo
import Trampa
import Magicas
from Monstruo import Monstruo
import Deck
import random

def cargar_cartas(archivo):
    cartas = []
    with open(archivo, 'r') as file:
        for linea in file:
            datos = linea.strip("\n").split('/')
            tipo_carta = datos[5].upper()

            if tipo_carta == "MONSTRUO":
                carta = Monstruo(
                    carta_id=int(datos[0]),
                    nombre=datos[1],
                    descripcion=datos[2],
                    atributo=datos[3],
                    tipo_monstruo=datos[4],
                    ataque=int(datos[6]),
                    defensa=int(datos[7])
                )
            elif tipo_carta == "MAGICA":
                carta = Magicas(
                    carta_id=int(datos[0]),
                    nombre=datos[1],
                    descripcion=datos[2],
                    incremento=int(datos[6]),
                    tipo_objetivo=datos[4]
                )
            elif tipo_carta == "TRAMPA":
                carta = Trampa(
                    carta_id=int(datos[0]),
                    nombre=datos[1],
                    descripcion=datos[2],
                    atributo_objetivo=datos[3]
                )
            else:
                continue

            cartas.append(carta)
        print(cartas)
    return cartas

h=cargar_cartas("cartas.txt")