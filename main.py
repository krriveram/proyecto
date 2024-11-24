from Proyecto.CartaYuGiOh import CartaYuGiOh
from TipoCarta import TipoCarta
from Atributo import Atributo
from TipoMonstruo import TipoMonstruo
import Trampa
import Magicas
import Monstruo

def cargar_cartas(archivo):
    cartas = []
    with open(archivo, 'r', encoding='utf-8') as archivo_cartas:
        for linea in archivo_cartas:
            texto_carta = linea.strip("\n").split('/')
            if len(texto_carta) == 8:
                carta_id = int(texto_carta[0])
                nombre = texto_carta[1]
                descripcion = texto_carta[2]
                tipo_carta = TipoCarta[texto_carta[5].strip("\n").upper()]
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

