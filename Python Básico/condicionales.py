"""print=("Como te llamas?")
nombre=input()

print=("Enque año naciste?")
year=int(input())

edad= 2021-year

if edad>18:
    print("hola",nombre,"eres muy viejo")
else:
    print("hola", nombre,"eres muy joven")"""
#---------------------------------------------------
"""print("Escribe tu nombre")
nombre=input()
if nombre=="Javi":
    print("Te llamas igual que yo")""" 

#---------------------------------------------------
"""print("Cuantos invitados hay?")

invitados=int(input())
if invitados >=5 and invitados<=10:
    print("hay fiesta")           
else:
    print("no hay fiesta")"""
#---------------------------------------------------

"""print("Adivina el número entre el 1 y 3") 
numero=input()
if numero=='1' or numero=='3':
    print("has fallado")
elif numero=='2':
    print("numero correcto")
else:
    print("no has elegido el numero correcto")"""
#----------------------------------------------------

print("dime un número")
num1=int(input())     
print("dime otro numero")
num2=int(input())

print("elige sumar(s), restar(r) o multiplicar(m)")
operacion=input()

if operacion=="s":
    print("el resultado es",num1+num2)
elif operacion=="r":
    print("el resultado es",num1-num2) 
elif operacion =="m":
    print("el resultado es", num1*num2)  
else:
    print("no has escogido la opción correcta")         
    