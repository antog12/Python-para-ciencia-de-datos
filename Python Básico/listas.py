"""lista_extraña=[2,"hola",3.5]
print(lista_extraña[0])"""

MiAula=[["Luis","Gema","Juan"],["Gema","Celeste","Raquel"]]
"""print(MiAula[1][2])
print(MiAula[1])
print(len(MiAula))
print(len(MiAula[1]))"""

#-----------------------------------------

#Calcular la letra del deni usando listas.

letraDni=['T' , 'R' , 'W' , 'A' , 'G' , 'M' , 'Y' , 'F' , 'P' , 'D' , 'X' , 'B' , 'N'
, 'J' , 'Z' , 'S' , 'Q' , 'V' , 'H' , 'L' , 'C' , 'K' , 'E' ]

print("Introdice tu número de dni sin letra")
numDni=int(input())
resto=numDni%23
print(resto)

resultado=letraDni[resto]

print("La letra de tu dni es", resultado)