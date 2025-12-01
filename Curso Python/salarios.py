class Persona:
    def __init__(self, nombre, edad, salario):
        # Atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        # Representación en texto de la persona
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"


# Crear instancias de Persona
Persona1 = Persona('Hitler', 45, 7000000)
Persona3 = Persona('Juanita', 35, 2000000)
Persona4 = Persona('Luchito', 28, 4000000)

# Lista de personas
lista_personas = [Persona1, Persona3, Persona4]

# Función para filtrar personas por salario
def filtrar_personas_por_salario(lista_personas, salario_minimo):
    """
    Filtra una lista de objetos Persona que tengan un salario mayor o igual al salario mínimo.

    Args:
        lista_personas (list): Lista de objetos Persona.
        salario_minimo (int): Salario mínimo para filtrar.

    Returns:
        list: Lista de objetos Persona que cumplen con el criterio.
    """
    # Filtrar usando list comprehension
    return [persona for persona in lista_personas if persona.salario >= salario_minimo]


# Ejemplo de uso: Filtrar personas con salario >= 2,000,000
salario_minimo = 4000000
personas_filtradas = filtrar_personas_por_salario(lista_personas, salario_minimo)

# Mostrar las personas filtradas
print(f"Personas con salario mayor o igual a {salario_minimo}:")
for persona in personas_filtradas:
    print(persona)
