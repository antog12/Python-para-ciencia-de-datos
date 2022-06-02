#calcular area  y perimetro de la circunferencia

import math

def areaperimetro(radio):
    perimetro = 2*math.pi*radio
    area=math.pi*radio**2
    return perimetro, area

print(areaperimetro(3))