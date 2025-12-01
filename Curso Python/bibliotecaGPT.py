# Clase Libro
class Libro:
    def __init__(self, codigo, nombre, autor):
        self.codigo = codigo
        self.nombre = nombre
        self.autor = autor
        self.activo = True  # Si el libro está disponible para préstamo
    
    def marcar_disponible(self):
        self.activo = True
    
    def marcar_no_disponible(self):
        self.activo = False
    
    def __str__(self):
        estado = "Disponible" if self.activo else "No disponible"
        return f"Libro: {self.nombre}, Autor: {self.autor}, Estado: {estado}"

# Clase Persona
class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []  # Lista de libros prestados
    
    def prestar_libro(self, libro):
        if libro.activo:
            libro.marcar_no_disponible()
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado el libro: {libro.nombre}")
        else:
            print(f"El libro {libro.nombre} no está disponible")
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.marcar_disponible()
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro: {libro.nombre}")
        else:
            print(f"{self.nombre} no tiene el libro {libro.nombre} en su posesión")

    def listar_libros_prestados(self):
        if self.libros_prestados:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"- {libro.nombre}")
        else:
            print(f"{self.nombre} no tiene libros prestados")

# Clase Gestion
class Gestion:
    def __init__(self):
        self.libros_disponibles = []  # Lista de todos los libros en la biblioteca
        self.libros_prestados = {}    # Diccionario para gestionar los préstamos (persona -> libros)
    
    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Libro '{libro.nombre}' agregado a la biblioteca")

    def prestar_libro_a_persona(self, persona, libro):
        if libro in self.libros_disponibles and libro.activo:
            persona.prestar_libro(libro)
            if persona.nombre not in self.libros_prestados:
                self.libros_prestados[persona.nombre] = []
            self.libros_prestados[persona.nombre].append(libro)
        else:
            print(f"El libro {libro.nombre} no está disponible para préstamo")
    
    def recibir_devolucion(self, persona, libro):
        if libro in self.libros_prestados.get(persona.nombre, []):
            persona.devolver_libro(libro)
            self.libros_prestados[persona.nombre].remove(libro)
        else:
            print(f"El libro {libro.nombre} no está registrado como prestado a {persona.nombre}")

    def listar_libros_disponibles(self):
        print("Libros disponibles en la biblioteca:")
        for libro in self.libros_disponibles:
            if libro.activo:
                print(f"- {libro}")

# Ejemplos de uso

# Crear libros
libro1 = Libro(1001, "Cien Años de Soledad", "Gabriel García Márquez")
libro2 = Libro(1002, "Don Quijote de la Mancha", "Miguel de Cervantes")
libro3 = Libro(1003, "El Principito", "Antoine de Saint-Exupéry")

# Crear personas
persona1 = Persona(1, "Ana")
persona2 = Persona(2, "Ramiro")

# Crear gestión de biblioteca
gestion = Gestion()

# Agregar libros a la biblioteca
gestion.agregar_libro(libro1)
gestion.agregar_libro(libro2)
gestion.agregar_libro(libro3)

# Listar libros disponibles
gestion.listar_libros_disponibles()

# Prestar libros a personas
gestion.prestar_libro_a_persona(persona1, libro1)  # Ana toma prestado "Cien Años de Soledad"
gestion.prestar_libro_a_persona(persona2, libro2)  # Ramiro toma prestado "Don Quijote"

# Listar libros prestados por Ana y Ramiro
persona1.listar_libros_prestados()
persona2.listar_libros_prestados()

# Devolver libro
gestion.recibir_devolucion(persona1, libro1)  # Ana devuelve "Cien Años de Soledad"
persona1.listar_libros_prestados()

# Listar libros disponibles después de la devolución
gestion.listar_libros_disponibles()
