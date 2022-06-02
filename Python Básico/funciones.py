"""def saludo():
    print("hola comtroleros y controleras")
    print("bienvenidos a nuestro curso de python")

saludo()    
saludo()
saludo()"""

#ahora quiero que como parámetro reciba la persona que esté
#en el curso.

def saludo(nombre):
    print("hola {}".format(nombre))
    print("bienvenidos a nuestro curso de python")

saludo("Fernando")    
saludo("Paula")

#vamos a hacer una función de resta

"""def resta(a,b):
    return a-b

c=resta(a=10,b=5) 
print("la resta es {}".format(c))"""
print("---------------------------------------")
def resta(a=None, b=None):
    if a==None or b==None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b

c=resta(10,2)    
print("La resta es {}".format(c))  

print("--------------------------------------")



def convertirGrados(temp,unidad):
    if unidad=="K" or unidad=="k":
        c=temp+273,15
    elif unidad=="F" or unidad=="f":
        c=temp * 1.8+32 
    else:
        print("Debes seleccionar una unidad que sea F o K")
        return
    return c

c=convertirGrados(17,"F")          
print("17 grados Cº equivalen a {}".format(c), "Farenheit")    

















