# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, nombre, modelo, matricula, precio):
        self.marca = marca
        self.nombre = nombre        
        self.modelo = modelo       
        self.precio = precio
        self.matricula = matricula
        self.disponible = True  # Todos los vehículos están disponibles por defecto
    
    def marcar_disponible(self):
        self.disponible = True
    
    def marcar_no_disponible(self):
        self.disponible = False
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Marca: {self.marca}, Nombre: {self.nombre}, Modelo: {self.modelo}, Matrícula: {self.matricula}, Precio: {self.precio}, Estado: {estado}"

# Clase derivada Auto (hereda de Vehiculo)
class Auto(Vehiculo):
        def __init__(self, marca, nombre, modelo, matricula, precio):
            super().__init__(marca, nombre, modelo, matricula, precio)
            
        def __str__(self):
            return super().__str__()
        
# Clase derivada Camion (hereda de Vehiculo)
class Camion(Vehiculo):
    def __init__(self, marca, nombre, modelo, matricula, precio, capacidad_carga):
        super().__init__(marca, nombre, modelo, matricula, precio)
        self.capacidad_carga = capacidad_carga
    
    def __str__(self):
        
        return super().__str__() + f", Capacidad de carga: {self.capacidad_carga} kg"


# Clase derivada Bicicleta (hereda de Vehiculo)
class Bicicleta(Vehiculo):
    def __init__(self, marca, nombre, modelo, precio, tipo):
        super().__init__(marca, nombre, modelo, None, precio)  # Las bicicletas no tienen matrícula
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"


# Clase Cliente
class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.propiedad_vehiculos = []  # Lista de vehículos que el cliente ha comprado
    
    def __str__(self):
        vehiculos = ", ".join([f"{vehiculo.nombre} ({vehiculo.matricula})" for vehiculo in self.propiedad_vehiculos]) if self.propiedad_vehiculos else "Ninguno"
        return f"ID: {self.id}. Nombre: {self.nombre}. Vehículos en propiedad: {vehiculos}"

    def listar_vehiculos(self):
        if self.propiedad_vehiculos:
            print(f"El cliente {self.nombre} tiene los siguientes vehículos:")
            for vehiculo in self.propiedad_vehiculos:
                print(f"- {vehiculo}")
        else:
            print(f"{self.nombre} no ha comprado ningún vehículo.")

    def calcular_valor_total(self):
        total = sum(vehiculo.precio for vehiculo in self.propiedad_vehiculos)
        return total

# Clase Gerencia
class Gerencia:
    def __init__(self):
        self.vehiculos = []  # Lista de vehículos en el inventario
        self.clientes = []  # Lista de clientes registrados
    
    # Método para registrar un cliente
    def registrar_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)
            print(f"Cliente {cliente.nombre} ha sido registrado exitosamente.")
        else:
            print(f"El cliente {cliente.nombre} ya está registrado.")

    # Método para listar todos los clientes
    def listar_clientes(self):
        if self.clientes:
            print("Clientes registrados:")
            for cliente in self.clientes:
                print(f"- {cliente}")
        else:
            print("No hay clientes registrados.")

    # Método para listar vehículos disponibles
    def vehiculos_disponibles(self):
        disponibles = [vehiculo for vehiculo in self.vehiculos if vehiculo.disponible]
        if disponibles:
            print("Vehículos disponibles en el inventario:")
            for vehiculo in disponibles:
                print(f"- {vehiculo}")
        else:
            print("No hay vehículos disponibles.")

    # Método para vender un vehículo
    def vender_vehiculo(self, vehiculo, cliente):
        if vehiculo.disponible:
            vehiculo.marcar_no_disponible()
            cliente.propiedad_vehiculos.append(vehiculo)
            print(f"El vehículo {vehiculo.nombre} ha sido vendido a {cliente.nombre}.")
        else:
            print(f"El vehículo {vehiculo.nombre} no está disponible para la venta.")
    
    # Método para devolver un vehículo
    def devolver_vehiculo(self, vehiculo, cliente):
        if vehiculo in cliente.propiedad_vehiculos:
            vehiculo.marcar_disponible()
            cliente.propiedad_vehiculos.remove(vehiculo)
            print(f"El vehículo {vehiculo.nombre} ha sido devuelto por {cliente.nombre}.")
        else:
            print(f"El cliente {cliente.nombre} no tiene el vehículo {vehiculo.nombre}.")

# Ejemplo de uso

# Crear algunos vehículos
auto1 = Auto('Renault', 'Logan', 2010, 'ABX511', 15000000)
camion1 = Camion('Volvo', 'FH16', 2019, 'VLV900', 80000000, 30000)
bicicleta1 = Bicicleta('Trek', 'Domane', 2021, 1000000, 'Carretera')

# Crear cliente
cliente1 = Cliente(103, 'Amber')
cliente2 = Cliente(104, 'John')

# Crear gerencia
gerencia = Gerencia()

# Agregar vehículos al inventario
gerencia.vehiculos.append(auto1)
gerencia.vehiculos.append(camion1)
gerencia.vehiculos.append(bicicleta1)

# Registrar clientes
gerencia.registrar_cliente(cliente1)
gerencia.registrar_cliente(cliente2)

# Listar clientes registrados
gerencia.listar_clientes()

# Listar vehículos disponibles en el inventario
gerencia.vehiculos_disponibles()

# Vender un vehículo a un cliente
gerencia.vender_vehiculo(auto1, cliente1)

# Mostrar la información del cliente después de la compra
print(cliente1)

# Listar vehículos del cliente
cliente1.listar_vehiculos()

# El cliente devuelve el vehículo
gerencia.devolver_vehiculo(auto1, cliente1)

# Listar vehículos disponibles en el inventario después de la devolución
gerencia.vehiculos_disponibles()

# Imprimir el estado de los vehículos
print(auto1)
print(camion1)
print(bicicleta1)
