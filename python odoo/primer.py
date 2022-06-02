"""numero= int(input("dime un numero"))
benito=300*numero
print(benito)"""

#Como se hace un if

"""numero = int(input("dime la edad"))
if(numero<18):
    print("Cuando seas padre comerás huevos")
else:
    print("preaprate para lo que viene")    """

"""respuesta= int(input("dime la contraseña"))
clave="Rebeca"  
if(respuesta==clave):
    print("Contraseña correcta")
else:
    print("contraseña incorrecta") """

#numero=2000
#otronumero=30

"""numero=int(input("dime un numero"))
otronumero=int(input("dime otro numero"))


pregunta=int(input("Escribe 1 para suma, 2 para resta , 3 para multiplicacion"))
if(pregunta==1):
    print(numero+otronumero)
elif(pregunta==2):
    print(numero-otronumero) 
elif(pregunta==3):
    print(numero*otronumero)"""

#repaso if

"""equipo1=input("dime el nombre del equipo 1")
goles1=int(input("dime los goles del equipo 1"))

equipo2=input("dime el nombre del equipo 2")
goles2=int(input("dime los goles del equipo 2"))

if(goles1>goles2):
    print("ha ganado el: "+ equipo1)
elif(goles2>goles1):
    print("ha ganado el: "+ equipo2) 
elif(goles1==goles2):
    print("Empate")  """

# FOR en python

"""lista=["hola","hello","allo","Ciao","hi"]   
nombre=input("dime tu nombre")

for elemento in lista:
    print(elemento + " "+ nombre)"""

#cuadrado
"""lista = [27,33,12,10]  
for elemento in lista:
    print(elemento*elemento)  """

#mostrar los mayores de 15

"""lista=[27,33,12,10]
for elemento in lista:
    if(elemento>15):
        print(elemento)"""

#suma de todos los elementos(acumulador)   

"""lista=[27,33,12,10] 
acumulador=0
for elemento in lista:
    acumulador=acumulador+elemento
    print("La suma es "+str(acumulador))"""

#Calcular el producto de todos los números

"""lista=[27,33,12,10]
acumulador=1 #ojo que tiene que ser 1 para multiplicación
for elemento in lista
acumulador=acumulador*elemento
    print("La suma es "+str(acumulador))"""

#Buscar valor en la lista

lista=[27,33,12,10] 
buscado= 12
posicion=0
encontrado=False
for elemento in lista:
    if(elemento==buscado):
        print("El elemento " + str(buscado) + " está en la posición "+str(posicion))
        encontrado=True
    posicion=posicion+1#aumnento la posición
if(not encontrado):
    print("el elemento no está en la lista")




   
            





