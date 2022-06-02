"""print("hagamos una lista de jugadores")
equipo=[]

print("introduce el nombre del primer jugador")
equipo.append(input())

print("introduce el nombre del segundo jugador jugador")
equipo.append(input())

print(equipo)"""

#------------------------------------

"""print("Hagamos una lista de jugadores")
equipo=[]

for i in range(3):
    print("Introduce el nombre del jugador ",i+1)
    equipo.append(input())
    print(equipo)

#print(equipo)  """

#-------------------------------------

"""print("estos son los numero pares entre el 1 y el 100")  

for i in range(1,101):
    if(i%2==0):
        print(i)"""

#-----------------------------------------
# Calculo de potencias

"""print("Escribe la base")        
base=int(input())
print("Escribe el exponente")
exponente=int(input())

acumulado=base

for i in range(exponente-1):
    acumulado=acumulado*base
print("El resultado es: ",acumulado) """

#-------------------------------------------

#Cuenta las letras que hay en una palabra

print("escribe una palabra en minusculas y sin tildes")
palabra=input()

acumulado=0

for i in palabra:
    if i=="a":
        acumulado=acumulado+1

print("el numero de aes es:",acumulado)        





















