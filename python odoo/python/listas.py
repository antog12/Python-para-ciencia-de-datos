#cuantas veces aparece un numero en una lista???

lista=[23,87,12,99,99,75,24]
numero=int(input("dime un numero"))
contador=0

for n in lista:
    if(n==numero):
        contador=contador + 1
print("El número ", numero, " aparece ",contador, " veces")

# contar los numeros pares que hay en la lista

lista=[23,87,12,99,99,75,24]
contadorPares=0
for n in lista:
    if(n % 2==0):
        contadorPares=contadorPares+1
print(contadorPares)        


