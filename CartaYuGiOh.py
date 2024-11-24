from Proyecto.Atributo import Atributo
from Proyecto.TipoCarta import TipoCarta
from Proyecto.TipoMonstruo import TipoMonstruo

class CartaYuGiOh:
  def __init__(self,carta_id, nombre, descripcion, atributo, tipoMounstro, tipoCarta, defensa, ataque):
    self.nombre = nombre
    self.descripcion = descripcion
    self.atributo = atributo
    self.tipoMonstruo = tipoMounstro
    self.tipoCarta = tipoCarta
    self.defensa = defensa
    self.ataque = ataque
    self.carta_id = carta_id
  
  def getNombre(self):
    return self.nombre
  def getDescripcion(self):
    return self.descripcion
  def getAtributo(self):
    return self.atributo
  def getTipoMonstruo(self):
    return self.tipoMonstruo
  def getTipoCarta(self):
    return self.tipoCarta
  def getDefensa(self):
    return self.defensa
  def getAtaque(self):
    return self.ataque
  def setNombre(self, nombre):
    self.nombre = nombre
  def setDescripcion(self, nombre):
    self.descripcion = nombre
  def setAtributo(self, nombre):
    self.atributo = nombre
  def setTipoMonstruo(self, nombre):
    self.tipoMonstro = nombre
  def setTipoCarta(self, nombre):
    self.tipoCarta = nombre
  def setDefensa(self, defensa):
    self.defensa = defensa
  def setAtaque(self, ataque):
    self.ataque = ataque
    
  def cargar_cartas(archivo):
    l_cartas = []
    archivo_cartas = open(archivo, 'r')
    for linea in archivo_cartas:
      texto_carta = linea.strip().split('/')
      if len(texto_carta)==8:
        carta_id = int(texto_carta[0])
        nombre = texto_carta[1]
        descripcion = texto_carta[2]
        atributo = Atributo[texto_carta[3].strip().lower()]
        tipoMonstruo = TipoMonstruo[texto_carta[4].strip().lower()]
        tipoCarta = TipoCarta(texto_carta[5])
        defensa = int(texto_carta[6])
        ataque = int(texto_carta[7])
        carta = CartaYuGiOh(carta_id, nombre, descripcion, atributo, tipoMonstruo, tipoCarta, defensa, ataque)
        l_cartas.append(carta)
    archivo_cartas.close()
    return l_cartas
  
  def __str__(self):
    return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nAtributo: {self.atributo}\nTipo de Monstruo: {self.tipoMonstruo}\nTipo de Carta: {self.tipoCarta}\nDefensa: {self.defensa}\nAtaque: {self.ataque}\n"


# Cargar las cartas desde el archivo 'cartas.txt'
cartas_creadas = CartaYuGiOh.cargar_cartas('cartas.txt')

# Imprimir las cartas creadas para verificar
for carta in cartas_creadas:
    print(carta)
      
    
  