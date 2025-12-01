class MiClase:
    
    def __init__(self, parametro):
        self.parametro = parametro  # Atributo público
        self.nombre = 'MiClase'     # Atributo público
        self._valor = 42            # Atributo protegido (convención: usar _ al inicio)
    
    def __str__(self):
        return f'MiClase(parametro={self.parametro}, nombre={self.nombre}, _valor={self._valor})'

obj = MiClase(456)
print(obj._valor)     # Funciona, pero la convención indica que no debería accederse directamente.
print(obj.nombre)     # Es una variable pública, se puede acceder libremente.
print(obj.parametro)  # También es pública.
print(obj)            # Se imprime el objeto.
print(MiClase(456).__str__()) # Se imprime el objeto.
print(obj.__str__) # Se imprime el objeto.