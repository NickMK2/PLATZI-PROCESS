# Clase Auto
class Auto:
    def __init__(self, marca, nombre, modelo, matricula, precio):
        self.marca = marca
        self.nombre = nombre        
        self.modelo = modelo       
        self.precio = precio
        self.matricula = matricula
        self.disponible = True  # El auto está disponible por defecto
    
    def marcar_disponible(self):
        self.disponible = True
    
    def marcar_no_disponible(self):
        self.disponible = False
        
    def obtener_precio(self):
        return self.precio
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Marca: {self.marca}, Nombre: {self.nombre}, Modelo: {self.modelo}, Matrícula: {self.matricula}, Precio: {self.precio}, Estado: {estado}"

# Clase Cliente
class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.propiedad_autos = []  # Lista de autos que el cliente ha comprado
    
    def __str__(self):
        autos = ", ".join([f"{auto.nombre} ({auto.matricula})" for auto in self.propiedad_autos]) if self.propiedad_autos else "Ninguno"
        return f"ID: {self.id}. Nombre: {self.nombre}. Autos en propiedad: {autos}"

    def listar_autos(self):
        if self.propiedad_autos:
            print(f"El cliente {self.nombre} tiene los siguientes autos:")
            for auto in self.propiedad_autos:
                print(f"- {auto}")
        else:
            print(f"{self.nombre} no ha comprado ningún auto.")

# Clase Gerencia
class Gerencia:
    def vender_auto(self, auto, cliente):
        # Verificar si el auto está disponible
        if auto.disponible:
            auto.marcar_no_disponible()  # Marcar el auto como no disponible
            cliente.propiedad_autos.append(auto)  # Agregar el auto a la lista de propiedad del cliente
            print(f"El auto {auto.nombre} ha sido vendido a {cliente.nombre}.")
        else:
            print(f"El auto {auto.nombre} no está disponible para la venta.")
    
    def devolver_auto(self, auto, cliente):
        # Verificar si el cliente tiene el auto en su propiedad antes de devolverlo
        if auto in cliente.propiedad_autos:
            auto.marcar_disponible()  # Marcar el auto como disponible de nuevo
            cliente.propiedad_autos.remove(auto)  # Remover el auto de la propiedad del cliente
            print(f"El auto {auto.nombre} ha sido devuelto por {cliente.nombre}.")
        else:
            print(f"El cliente {cliente.nombre} no tiene el auto {auto.nombre}.")
    
    def autos_disponibles(self, autos):
        # Mostrar los autos disponibles en el inventario
        disponibles = [auto for auto in autos if auto.disponible]
        if disponibles:
            print("Autos disponibles en el inventario:")
            for auto in disponibles:
                print(f"- {auto}")
        else:
            print("No hay autos disponibles.")

# Ejemplo de uso

# Crear autos
auto1 = Auto('Renault', 'Logan', 2010, 'ABX511', 15000000)
auto2 = Auto('Ford', 'Mustang', 2022, 'XYZ123', 30000000)

# Crear cliente
cliente1 = Cliente(103, 'Amber')

# Crear gerencia
gerencia = Gerencia()

# Listar autos disponibles en el inventario
gerencia.autos_disponibles([auto1, auto2])

# Vender un auto a un cliente
gerencia.vender_auto(auto1, cliente1)

# Mostrar la información del cliente después de la compra
print(cliente1)

# Listar autos del cliente
cliente1.listar_autos()

# Imprimir el estado del auto después de la compra
print(auto1)

# El cliente devuelve el auto
gerencia.devolver_auto(auto1, cliente1)

# Listar autos disponibles en el inventario después de la devolución
gerencia.autos_disponibles([auto1, auto2])

# Imprimir el estado del auto después de la devolución
print(auto1)
