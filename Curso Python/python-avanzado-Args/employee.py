class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs
    
    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Skills', self.skills)
        print('Details', self.details)

employee = Employee('Carlos', 'Python', 'Java', 'C++', age=30, city = 'Bogotá')
employee.show_employee()
employee2 = Employee('Carlos', 'Python', 'Java', 'C++', age=30, city = 'Bogotá', country = 'Colombia')
Employee.show_employee(employee2)
 