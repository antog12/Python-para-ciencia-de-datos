nombres=["Paco","Maria","Raquel"]
print("lista previa")
print(nombres)
print("Dame el elemento a añadir")
nuevo=input()
nombres.append(nuevo)#añade el elmento al final
print("nombres despues de añadir el elemento")
print(nombres)
nombres.insert(2,"Julian")
print("Nombres finales")
print(nombres)