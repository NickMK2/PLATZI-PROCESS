
def despues(funcion):
    def wrapper(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        print("Después de la función")
        return resultado
    return wrapper

def antes(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        return funcion(*args, **kwargs)
    return wrapper

@antes
@despues
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")
saludar("Rodrigo")
saludar("Urielcito")