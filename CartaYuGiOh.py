from tipo_carta import TipoCarta
from atributos import Atributo
from tipo_monstruo import TipoMonstruo
from tipo_carta import TipoCarta

class CartaYuGiOh:
    def __init__(self, nombre, descripcion, tipo_carta):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo_carta = tipo_carta

    @classmethod
    def desde_linea(cls, linea):
        """
        Constructor de clase para crear una carta desde una línea del archivo .txt.
        """
        datos = linea.strip().split('/')
        tipo_carta = datos[5].upper()

        if tipo_carta == "MONSTRUO":
            from atributos import Atributo
            from tipo_monstruo import TipoMonstruo
            return Monstruo(
                nombre=datos[1],
                descripcion=datos[2],
                atributo=Atributo[datos[3].upper()],
                tipo_monstruo=TipoMonstruo[datos[4].upper()],
                ataque=int(datos[6]),
                defensa=int(datos[7])
            )
        elif tipo_carta == "MAGICA":
            return Magicas(
                nombre=datos[1],
                descripcion=datos[2],
                incremento=int(datos[6]),
                tipo_objetivo=datos[4]
            )
        elif tipo_carta == "TRAMPA":
            from atributos import Atributo
            return Trampa(
                nombre=datos[1],
                descripcion=datos[2],
                atributo_objetivo=Atributo[datos[3].upper()]
            )
        else:
            raise ValueError(f"Tipo de carta desconocido: {tipo_carta}")

    def __str__(self):
        return f"{self.nombre} ({self.tipo_carta}): {self.descripcion}"


      
    
  
