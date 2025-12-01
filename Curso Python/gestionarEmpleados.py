class Empleado:
    empleados = []  # Variable de clase
    
    def __init__(self, nombre, salario, id, edad):
        self.nombre = nombre  # Variable de instancia
        self.salario = salario  # Variable de instancia
        self.id = id  # Variable de instancia
        self.edad = edad  # Variable de instancia
    
    def agregarEmpleado(self):
        Empleado.empleados.append(self)  # Acceso a variable de clase
        
    def eliminarEmpleado(self):
        Empleado.empleados.remove(self)  # Acceso a variable de clase
    
    def mostrarEmpleado(self):
        print('Nombre: {self.nombre}, Salario: {self.salario}, ID: {self.id}, Edad: {self.edad}'.format(self=self))
        

if __name__ == '__main__':
    empleado1 = Empleado('Juan', 30000, 1, 25)
    empleado1.agregarEmpleado()
    
    empleado2 = Empleado('Ana', 35000, 2, 30)
    empleado2.agregarEmpleado()
    
    empleado3 = Empleado('Luis', 40000, 3, 35)
    empleado3.agregarEmpleado()
    
    empleado4 = Empleado('Maria', 45000, 4, 40)
    empleado4.agregarEmpleado()
    
    print('Empleados:')
    for empleado in Empleado.empleados:
        empleado.mostrarEmpleado()
    
    empleado2.eliminarEmpleado()
    
    print('Empleados:')
    for empleado in Empleado.empleados:
        empleado.mostrarEmpleado()