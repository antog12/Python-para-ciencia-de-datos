#tengo una lista de numeros positivos y negativos. quiero que me diga lo que suma los positivos y los negativos
lista=[-3,-2,1,-2,23,-233,29,88]
negativos=0
positivos=0

for numero in lista:
    if(numero>0):
        positivos= positivos + numero
    elif(numero<0):
        negativos= negativos + numero  
print("Los negativos suman", negativos)      
print("los positivos suman", positivos)    

