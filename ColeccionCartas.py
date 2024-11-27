from Monstruo import Monstruo
from Magicas import Magicas
from Trampa import Trampa
from pathlib import Path

class ColeccionCartas:
    def __init__(self):
        self.cartas = []
    def cargarCartas(self, archivo):
        try:
            rutaArhcivo = Path(archivo)
            rutaAbsoluta = rutaArhcivo.resolve()

            with open(rutaAbsoluta, 'r', encoding = 'utf=8') as file:
                for linea in file:
                    partes = linea.strip().split('/')

                    if partes[0] == 'monstruo':
                        nombre = partes[1]
                        descripcion = partes[2]
                        ataque = partes[3]
                        defensa = partes[4]
                        carta = Monstruo(nombre, descripcion, ataque, defensa)
                    
                    elif partes[0] == 'magica':
                        nombre = partes[1]
                        descripcion = partes[2]
                        tipo_objetivo = partes[3]
                        incremento = partes[4]
                        carta = Magicas(nombre, descripcion, tipo_objetivo, incremento)
                    
                    elif partes[0] == 'trampa':
                        nombre = partes[1]
                        descripcion = partes[2]
                        tipo_objetivo = partes[3]
                        carta = Trampa(nombre, descripcion, tipo_objetivo)
                    
                    self.cartas.append(carta)
        except FileNotFoundError:
            print(f"Error: el archivo no se encontro")
        except Exception as e:
            print(f" Ocurrio un error: {e}")
        
    def mostrarCartas(self):
        for carta in self.cartas:
            print(carta)

coleccion = ColeccionCartas()
coleccion.cargar_cartas('txt/archivo.txt')

# Mostrar las cartas cargadas
coleccion.mostrar_cartas()