from TipoCarta import TipoCarta
from Atributo import Atributo
from TipoMonstruo import TipoMonstruo
import Trampa
import Magicas

class CartaYuGiOh:
    
    def __init__(self, nombre, descripcion, tipo_carta,ataque,defensa):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo_carta = tipo_carta
        self.ataque=ataque
        self.defensa=defensa
    