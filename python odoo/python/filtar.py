#guardar en la lista 2 los elemntos mayores que 30
lista=[23,45,19,93,72,11,10]
lista2=[]

for numero in lista:
    if (numero>30):
        lista2.append(numero)
print(lista2)

#decir si un numero esta en la lista,pregunto un numero y digo si está en la list
lista=[23,45,19,93,72,11,10]
numero=int(input("dime un número"))
noencontrado=True
for i in lista:
    if(i==numero):
        print("el numero está en la lista")
        noencontrado=False

if(noencontrado):
    print("no se ha encontrado el numero")


#suma de la lista
lista=[23,45,19,93,72,11,10]
resultado=0
for numero in lista:
    resultado=  resultado + numero
print(resultado)    





