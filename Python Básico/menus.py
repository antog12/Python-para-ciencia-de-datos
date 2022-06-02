#vamos a crear menus dentro de python

menu="""Bienvenido al registro de usuarios, seleccione el campo que desee:
[1] Diga su nombre
[2] Diga su edad
[3] diga si email"""

print(menu)

opcion=input("Seleccione entre 1 y 3: ")

if opcion=='1':
    nombre=input("Escriba su nombre: ")
    if nombre.isalpha()== True:
        print("tu nombre es {}".format(nombre))
    else:
        print("Has escrito un nombre no válido...")        
    

elif opcion =='2':
    edad=input("Escriba su edad: ")
    if edad.isnumeric:
        print("Tu edad es {}".format(edad))
    else:
        print("Has introducido una edad no válida")    
    
elif opcion=='3':
    email=input("escribe tu email: ")
    if email.find("@")>=0 and email.find(".")>=0:
        print("Tu email es {}".format(email))
    else:
        print("Has introducido un email no válido...")    

else:
    print("debes de elegir entre 1 y 3")
    print("=-=*")
