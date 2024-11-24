from Proyecto.Atributo import Atributo
from Proyecto.TipoCarta import TipoCarta
from Proyecto.TipoMonstruo import TipoMonstruo

class CartaYuGiOh:
  def __init__(self, carta_id, nombre, descripcion, tipo_carta):
    self.carta_id = carta_id
    self.nombre = nombre
    self.descripcion = descripcion
    self.tipo_carta = tipo_carta
  
  def getNombre(self):
    return self.nombre
  def getDescripcion(self):
    return self.descripcion
  def getTipoCarta(self):
    return self.tipoCarta
  
  def setNombre(self, nombre):
    self.nombre = nombre
  def setDescripcion(self, nombre):
    self.descripcion = nombre
  def setTipoCarta(self, nombre):
    self.tipoCarta = nombre

  def __str__(self):
    return f"Nombre: {self.nombre}\nDescripcion: {self.descripcion}\nTipo de Carta: {self.tipoCarta}"


      
    
  
