#nos dan un texto "hola" y tenemos que espaciarlo h o l a .

def espaciado(cadena):# cadena es el parametro que vamosa pasar luego. en este caso es hola.
    resultado=""
    for letra in cadena:
        resultado = resultado + letra + " "

    return resultado

print(espaciado("hola"))    