from CartaYuGiOh import Monstruo, Magica, Trampa
import random as rd
from pathlib import Path

class Deck:
    def __init__(self, cartas):
        self.cartas = cartas

    def robarCarta(self):
        if self.cartas:
            return self.cartas.pop(0)
        else:
            return None

    @staticmethod
    def cargar_cartas():
        archivo = "txt/archivo.txt"
        ruta_archivo = Path(archivo)
        ruta_absoluta = ruta_archivo.resolve()

        cartas = []

        try:
            with open(ruta_absoluta, 'r', encoding='utf-8') as file:
                for linea in file:
                    partes = linea.strip().split('/')
                    
                    if partes[0].lower() == "monstruo" and partes[6]:
                        if len(partes) < 7:
                            print(f"Error: Falta información en la línea: {linea}")
                            continue
                        nombre = partes[1]
                        descripcion = partes[2]
                        ataque = partes[3]
                        defensa = partes[4]
                        atributo = partes[5]
                        tipo_monstruo = partes[6]
                        carta = Monstruo(nombre, descripcion, ataque, defensa, atributo, tipo_monstruo)
                    elif partes[0].lower() == "magica":
                        if len(partes) < 5:
                            print(f"Error: Falta información en la línea: {linea}")
                            continue
                        nombre = partes[1]
                        descripcion = partes[2]
                        tipo_objetivo = partes[3]
                        incremento = partes[4]
                        carta = Magica(nombre, descripcion, tipo_objetivo, incremento)
                    elif partes[0].lower() == "trampa":
                        if len(partes) < 4:
                            print(f"Error: Falta información en la línea: {linea}")
                            continue
                        nombre = partes[1]
                        descripcion = partes[2]
                        tipo_objetivo = partes[3]
                        carta = Trampa(nombre, descripcion, tipo_objetivo)
                    else:
                        print(f"Tipo de carta desconocido: {partes[0]}")
                        continue

                    cartas.append(carta)
        except FileNotFoundError:
            print(f"Error: El archivo '{archivo}' no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

        return cartas

    @staticmethod
    def generar_deck():
        todas_las_cartas = Deck.cargar_cartas()
        cartas_deck = rd.sample(todas_las_cartas, min(30, len(todas_las_cartas)))
        return Deck(cartas_deck)

    def barajar(self):
        rd.shuffle(self.cartas)
        print("El deck ha sido barajado.")

    def mostrar_cartas(self):
        for carta in self.cartas:
            print(f"{carta.nombre} - {carta.tipo}")
cartas=0