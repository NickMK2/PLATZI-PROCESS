class BaseClass:
    def __init__(self, publica):
        self.publica = publica
        self._protected_variable = 'Protected'
        self.__private_variable = 'Private'
        self.__private_variable2 = 'Private2'

    def _protected_method(self):
        print('Este es un metodo protegido')

    def __private_method(self):
        print('Esto es un metodo privado')

    def public_method(self):
        self.__private_method()

base = BaseClass('Variable publica')
print(base.publica)
print(base._protected_variable)
print(base._BaseClass__private_variable)  # 'Private'
print(base._BaseClass__private_variable2) # 'Private2'
base._protected_method()
base.public_method()