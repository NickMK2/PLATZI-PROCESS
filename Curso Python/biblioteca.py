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
        return f"Libro: {self.nombre}. Estado: {estado}. Código: {self.codigo}"

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
            print(f"El libro '{libro.nombre}' fue prestado a {self.nombre}")
        else:
            print(f"El libro '{libro.nombre}' no está disponible.")
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.marcar_disponible()
            self.libros_prestados.remove(libro)
            print(f"Libro devuelto: '{libro.nombre}' por {self.nombre}")
        else:
            print(f"{self.nombre} no tiene prestado el libro '{libro.nombre}'.")

    def lista_prestamo(self):
        if self.libros_prestados:
            print(f"Libros prestados a {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"- {libro.nombre}")
        else:
            print(f"{self.nombre} no tiene libros prestados")


# Clase Gestion
class Gestion:
    def __init__(self):
        self.libros_disponibles = []  # Lista de todos los libros en la biblioteca
    
    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        print(f"Libro '{libro.nombre}' agregado a la biblioteca")
    
    def asignar_prestamo_persona(self, persona, libro):
        if libro in self.libros_disponibles and libro.activo:
            persona.prestar_libro(libro)
        else:
            print(f"El libro '{libro.nombre}' no está disponible para préstamo.")
    
    def gestion_devoluciones(self, persona, libro):
        persona.devolver_libro(libro)

    def listar_libros_disponibles(self):
        print("Libros disponibles en la biblioteca:")
        for libro in self.libros_disponibles:
            if libro.activo:
                print(f"- {libro}")
    
# Ejemplo de uso

# Crear libros
libro1 = Libro(1, "100 Días", "Roberto Carlos")
libro2 = Libro(2, "La vida es bella", "Roman")

# Crear personas
persona1 = Persona(1, "Ana")
persona2 = Persona(2, "Ramiro")

# Crear gestion de biblioteca
gestion = Gestion()

# Agregar libros a la biblioteca
gestion.agregar_libro(libro1)
gestion.agregar_libro(libro2)

# Listar libros disponibles
gestion.listar_libros_disponibles()

# Prestar libros
gestion.asignar_prestamo_persona(persona1, libro1)  # Ana toma prestado "100 Días"
persona1.lista_prestamo()  # Ana lista los libros prestados

# Intentar prestar libro que ya no está disponible
gestion.asignar_prestamo_persona(persona2, libro1)  # Ramiro intenta tomar "100 Días"

# Devolver el libro y hacerlo disponible nuevamente
gestion.gestion_devoluciones(persona1, libro1)
gestion.listar_libros_disponibles()
