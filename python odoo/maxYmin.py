#calcular max y min

def maxMin(lista):
    max=lista[0]
    min=lista[0]
    for n in lista:
        if(n>max):
            max=n
        if(n<min):
            min=n
    print("el max es: ", max)
    print("El min es: ",min)    
    return max,min

    

print(maxMin([1,3,56,7,89]))