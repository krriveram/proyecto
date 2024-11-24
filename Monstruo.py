from CartaYuGiOh import CartaYuGiOh

class Monstruo:

  class Monstruo(CartaYuGiOh):
      def __init__(self, nombre, descripcion, atributo, tipo_monstruo, ataque, defensa):
        super().__init__(nombre, descripcion, TipoCarta.MONSTRUO)
        self.atributo = atributo
        self.tipo_monstruo = tipo_monstruo
        self.ataque = ataque
        self.defensa = defensa
        self.modo = True
  def atacar(self, enemigo):
      if enemigo.modo:
          return self.ataque - enemigo.ataque
      else:
          return self.ataque - enemigo.defensa

  def cambiar_modo(self):
      self.modo = not self.modo

  def get_modo(self):
      return self.modo
