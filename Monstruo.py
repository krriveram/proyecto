from CartaYuGiOh import CartaYuGiOh
import numpy as np

class Monstruo(CartaYuGiOh):
    def __init__(self, nombre, descripcion, tipo_carta,ataque,defensa,tipoAtributo,tipoMonstruo):
        super().__init__(self, nombre, descripcion, tipo_carta,ataque,defensa)
        self.tipoAtributo=tipoAtributo
        self.tipoMonstruo=tipoMonstruo


    def atacar(self, enemigo):
        if enemigo.modo:
            return self.ataque - enemigo.ataque
        else:
            return self.ataque - enemigo.defensa

    def cambiar_modo(self):
        self.modo = not self.modo

    def get_modo(self):
        return self.modo
    
    def __str__ (self):

        if(self.modo=="ataque"):
            if(self.boca_arriba==True and "vertical"=="vertical"):
                arriba=[" * "]
                cont=self.nombre.split(' ')
                for i in range(len(cont)):
                    arriba.append(" * ")
                arriba.append(" * ")
                aRab=np.array(arriba)
                print(aRab)
                print(f"\n\n\n nombre:"+self.nombre+"\n ataque:"+self.ataque+"\n defensa:"+self.defensa+"\n atributo:"+self.atributo+"\n monstruo:"+self.tipo_monstruo+"\n\n\n")
                print(aRab)
            else:
                M=np.array([[" *", " * ", " * ", " * ", "*"],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "Yu", "Gi", "Oh"," ! "],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "  ", "  ", "  ", " * "],
[" * ", "  ", "  ", "  ", " * "],
["*", " * ", " * ", " * ", "*"]]
)
                print(M)


            #MODELADO
            #vertical
            #boca arriba

            #* * * * * * * *  * * * * * * * * * * *
            #* nombre: Dragón Negro de Ojos Rojos *
            #* ataque: 2000                       *
            #* tipo Atributo: OSCURIDAD           *
            #* tipo Monstruo: DRAGON              *
            #* * * * * * * *  * * * * * * * * * * *

            #boca abajo
            #* * * * * * * *  * * * * *
            #*                        *
            #*                        *
            #*                        *
            #*       Yu-Gi-Oh         *
            #*                        *
            #*                        *
            #*                        *
            #* * * * * * * *  * * * * *


            #horizontal

            #boca arriba

            #* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
            #*  nombre: Dragón Negro de Ojos Rojos ,defensa: 2400, tipo Atributo: OSCURIDAD , tipo Monstruo: DRAGON *
            #* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 




