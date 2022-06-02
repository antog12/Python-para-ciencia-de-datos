class Alumno():
    contador=0
    def __init__(self, nombre, apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
        Alumno.contador += 1

    def mostrar(self):
        print(self.nombre)

alumno1 = Alumno("josé","sanchez")
print(alumno1.contador)
alumna1=Alumno("María","Guirao")
print(alumno1.contador)

print(alumno1.nombre, alumno1.apellidos)
print(alumna1.nombre, alumna1.apellidos)

