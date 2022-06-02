class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre= nombre
        self.edad= edad
        self.dni= dni

    

    def setEdad(self, edad):
        self.edad= edad
    
    def setDni(self, dni):
        self.dni= dni

    def setNombre(self, nombre):
        self.nombre= nombre

    def getEdad(self):
         return self.edad

    def getDni(self):
         return self.dni

    def getNombre(self):
         return self.nombre

    def mostrar(self):
        print(self.nombre, self.dni, self.nombre)

    def esmayordeEdad(self):
        return self.edad>18

persona1=Persona("Laura",19,"48488582m")
persona1.mostrar()
print("Es mayor?", persona1.esmayordeEdad())


        