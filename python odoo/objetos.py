import math


class punto():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def distancia(self, otro):
        """devuelve la distancia entrrea ambos puntos"""

        dx= self.x - otro.x
        dy= self.y - otro.y
        return math.sqrt((dx**2 + dy**2))


punto1= punto(1,2)
punto2= punto(1,2)

print("la distancia es ",punto1.distancia(punto2))
       


