class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def saludo(self):
        print(f"Hola mi nombre es {self.nombre}{self.apellido} y tengo {self.edad} annos")
        
Persona1 = Persona("Rambri","Guajiro",33)
Persona2 = Persona("Mambo","Jiro",34)

Persona1.saludo()
Persona2.saludo()