import random

def palabraAleatoria():
    palabras=["murcielago", "chocolate", "patata", "bastos", "cerebro"]
    aleatorio=random.randint(0, len(palabras)-1)#devielve un num aleatorio entre 1 y 10
    return palabras[aleatorio]

def palabraoculta(palabra):
    oculta=""
    for letra in palabra:
        oculta = oculta + "$"  
    return(oculta)      

#quiero quye me imprima en vez d la palabra, que me imprma asteriscos
mipalabra=palabraAleatoria() 
print(mipalabra)   
print(palabraoculta(mipalabra))    
print(palabraAleatoria())

#cambiar la letra oculta por la que se correponde
def comprobarLetra(oculta,palabra, letra):
    devolver=""
    for posicion in range(0, len(palabra)):
        if(palabra[posicion]==letra):
            devolver=devolver + letra
        else:
            devolver= devolver + oculta[posicion]    

    return devolver       

mipalabra=palabraAleatoria()
oculta=palabraoculta(mipalabra)
fallos=0
while ("$" in oculta and fallos<3):
    print(oculta)
    letra=input("dime una letra")
    aux=oculta
    oculta=comprobarLetra(oculta,mipalabra,letra)
    if(aux==oculta):
        fallos=fallos+1
    print("fallos ", fallos)    






  




