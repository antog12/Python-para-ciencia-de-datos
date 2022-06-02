from re import S


lista = ["lunes", "martes", "miercoles","jueves", "viernes",40,5.67,[1,2,3],True]

print(lista)

# vamos a agregar valores
print(lista)
#mostrar un elemento concreto de la lista
print(lista[0])
#si queiro que acceda desde el ultimo elemento
print(lista[-1])
#vamos a decir que me imprima desde el indice 0 hasta el 2(sublistas)
print(lista[0:3])#tienes que poner siempre un indice mas,es decir, desde el que tu le indicques hasta el anterior del valor final
#si no le indicamos a python desde donde queremos empezar, lo hará desde la posición 0
print(lista[:4])
#también desde el que le indique hasta el final
print(lista[2:])
#también podemos poner otros tipos de datos 
print(lista)

print("-------------------------------------")

#vamos a ver cuantos elementos tiene una lista

print(len(lista))
#más ejemplos
lista2=[1,2,3,4,5]
lista2.append(6)
lista2.append("Anto")
print(lista2)

#agregar un elemento en una posición especifica

lista3=[1,2,4,5]
lista3.insert(2,3)#en el indice 2 quiero que almacene el valor de 3
print(lista3)

#para iingresar varios elementos de golpe al final de tu lista

lista3.extend([6,7,8])
print(lista3)

#vamos a sumar dos listas

lista4=[1,2,3,4,5]
lista5=[6,7,8]
lista6=lista4+lista5
print(lista6)


#vamos a buscar un determinado elemento en una lista

lista7=[1,2,3,4,5,"Anto"]
print(3 in lista7)
print("Anto" in lista7)# si no está nos sale falso

#para saber en que índice se ubica un elemnto de una lista

print(lista7.index(5))# le paso el valor que quiero buscar, sino está,me lanza una excepción(lo vermos más adelante)
print(lista7.index("Anto"))

#para ver valores repetidos

lista7=[1,2,3,4,5,"Anto",1,2,3,4,"Anto",1]
#Cuantos valores 1 existen en la lista???
print(lista7.count(1))# el 1 aparece 3 veces
print(lista7.count("Anto"))#Anto aprece 2 veces

#como eleminir de la lista

lista7.pop()#esta función se carga el uktimo elemento que encuentre en la lista
print(lista7)# se carga el 1

#podemos pasarle un parámetro con el indice que quiero cargarme

lista7.pop(3)#elimina el indice
print(lista7)


#quiero eliminar un elemento pero no se el indice suyo

lista7.remove(5)
print(lista7)# vemos que me ha eliminado el 5

#para borrar toda la lista uso el métod clear

lista7.clear()
print(lista7)


#para ver la lista al revéS

lista8=[1,2,3,4,5,"Anto"]

lista8.reverse()   
print(lista8)

#copiar 2 veces los elementos de una lista

lista8=[1,2,3,4,5,"Anto"]*2
print(lista8)

#para ordenar los elementos de una lista

lista9=[5,4,-7,9,0,1,3]
lista9.sort()
print(lista9)


#vamos a ordenar los elementos de la lista de mayor a menor

lista9.sort(reverse=True)# de esta forma los elementos de la lista quedan ordenados al contrario
print(lista9)











































