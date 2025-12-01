class SerVivo ():
    def __init__(self, nombre):
        self.nombre = nombre

class Humano (SerVivo):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad

class Estudiante (Humano):
    def __init__(self, nombre, edad, id):
        super().__init__(nombre, edad)
        self.id = id

