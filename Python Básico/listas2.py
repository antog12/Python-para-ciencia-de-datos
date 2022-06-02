objetos=[7,"Hola", True, 3.5]
print(len(objetos))
objetos.append(14.26)
print(objetos)
print(len(objetos))
objetos.extend([5])
print(objetos)
objetos.extend(range(10,13))#con esto añadimos los numeros que queramos de golpe
print(objetos)
#count para ver cuantas veces se repite un elemento dentro de mi lista
objetos.count(5)
print(objetos.count(5))
#insert es para poder insertar objetos en la posicion que yo quiera
objetos.insert(2,"casa")#en la posicion 2 insero casa
print(objetos)
#remove es para eliminar elementos
objetos.remove(True)
print(objetos)
#pop es lo mismo que remover per en este caso es para los indices
objetos.pop(0)
print(objetos)
#index es para saber cual es el indice del elemento de la lista
objetos.index(10)
print(objetos.index(10))
#reverse es para invertir todos los objetos que tenemos en la lista
objetos.reverse()
print(objetos)
#sort organiza los elementos de menor a mayor
objetos.remove("Hola")
objetos.remove("casa")
print(objetos)
objetos.sort()
print(objetos)




