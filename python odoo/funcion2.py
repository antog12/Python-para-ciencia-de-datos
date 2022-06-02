#funcion que diga si es mayor o menor

def esmayor(n1,n2):
    if(n1>n2):
        print(str(n1)+" es mayor que "+str(n2))
    elif(n1<n2):
        print(str(n2)+" es mayor que "+str(n1))
    else:
        print("son iguales")

numero1= (int)(input("dime un numero")) 
numero2= (int)(input("dime otro numero")) 

esmayor(numero1,numero2)

    
