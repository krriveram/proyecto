from CartaYuGiOh import CartaYuGiOh
from TipoCarta import TipoCarta
from Atributo import Atributo
from TipoMonstruo import TipoMonstruo
import Trampa
import Magicas
from Monstruo import Monstruo
import Deck
import random

'''
def cargar_cartas(archivo):
    cartas = []
    with open(archivo, 'r') as archivo_cartas:
        for linea in archivo_cartas:
            texto_carta = linea.strip("\n").split('/')
            if len(texto_carta) == 8:
                carta_id = int(texto_carta[0])
                nombre = texto_carta[1]
                descripcion = texto_carta[2]
                tipo_carta = TipoCarta[texto_carta[5].upper()]
                if tipo_carta == TipoCarta.MONSTRUO:
                    atributo = Atributo[texto_carta[3].strip("\n").upper()]
                    tipo_monstruo = TipoMonstruo[texto_carta[4].strip("\n").replace(" ", "_").upper()]
                    defensa = int(texto_carta[6])
                    ataque = int(texto_carta[7])
                    carta = Monstruo(carta_id, nombre, descripcion, atributo, tipo_monstruo, defensa, ataque)
                elif tipo_carta == TipoCarta.MAGICA:
                    incremento = int(texto_carta[6])
                    tipo_objetivo = TipoMonstruo[texto_carta[4].strip("\n").replace(" ", "_").upper()]
                    carta = Magicas(carta_id, nombre, descripcion, incremento, tipo_objetivo)
                elif tipo_carta == TipoCarta.TRAMPA:
                    atributo_objetivo = Atributo[texto_carta[3].strip("\n").upper()]
                    carta = Trampa(carta_id, nombre, descripcion, atributo_objetivo)
                cartas.append(carta)
    return cartas

'''

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