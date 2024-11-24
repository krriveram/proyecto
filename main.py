from Proyecto.CartaYuGiOh import CartaYuGiOh
cartas = CartaYuGiOh.cargar_cartas('cartas.txt')
for carta in cartas:
  print(carta)