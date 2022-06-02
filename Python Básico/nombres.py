#Introduce nombres por teclado en una lista hasta que se introduzca un cero. 
# Muestra la lista. Pregunta un nombre para eliminar. Lo elimina de la lista y muestra la lista.

lista=[]
nombre="x"
eliminar="y"

while(nombre!="0"):
    nombre=input("Escribe un nombre: ")
    lista.append(nombre)
print("los nombres son: ",lista)
print("-------------------------")
eliminar=input("Dime el nombre que deseas eliminar: ")
lista.remove(eliminar)
print("La nueva lista es: ",lista)

#podemos poner también un control por si queremos controlar
#que el nombre esté o no en la lista...
#lo pondriamos debajo del nombre que deseamos eliminar.

"""if (eliminar in lista):
    lista.remove(eliminar)
    print("el nombre ha sido eliminado")
else:
    print("el nombre no está en la lista")
print("La nueva lista es: ",lista)"""
