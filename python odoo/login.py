#crear un login

from cgitb import reset


def login(usuario,clave, numIntentos):
    resultado=False
    if(usuario=="usuario1" and clave=="2asdasd"):
        resultado = True
    else:
        numIntentos = numIntentos - 1 # vamos restanto el num de intentos
        resultado = False
    return resultado,numIntentos

restantes =3# tenemos 3 intentos
usuario=""
clave=""
logueado=False
while(restantes>0 and  not logueado):
    usuario=input("dime el usuario")
    clave= input("dime la clave")
    resultado=login(usuario,clave, restantes)
    logueado=login(usuario,clave, restantes)[0]
    restantes=login(usuario,clave, restantes)[1]

if(logueado):
    print("estas dentro")
else:
    print("no sabes la clave")