class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary 

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salary = new_salary

    @salary.deleter
    def salary(self):
        print(f"El salario de {self.name} ha sido eliminado")
        del self._salary

# Crear instancia de Employee
employee = Employee("Ana", 5000)
print(f"Nombre: {employee.name}, Salario: {employee.salary}")
employee2 = Employee("Luis", -7000)
print(f"Nombre: {employee2.name}, Salario: {employee2.salary}")
print("-"*20)

# Modificar el salario de forma controlada
print('Modificando el salario de forma controlada...')
employee.salary = 6000
print(f"Nombre: {employee.name}, Salario: {employee.salary}")
employee2.salary = 8000
print(f"Nombre: {employee2.name}, Salario: {employee2.salary}")
print("-"*20)

# Intentar establecer un salario negativo
#employee.salary = -1000  

# Eliminar el salario
print('Eliminando el salario...')
del employee.salary  
del employee2.salary