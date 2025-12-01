def validar_ingreso(func):
    def envoltura(persona):
        if persona['Edad'] >= 18:
            func(persona['Nombre'])
        else:
            print(f"Lo siento {persona['Nombre']}, no puedes ingresar al club")
    return envoltura

@validar_ingreso    
def ingreso_club(nombre):
    print(f"Bienvenido al club: {nombre}")
    
persona1 = {'Nombre': 'Juan', 'Edad': 15}
persona2 = {'Nombre': 'Pedro', 'Edad': 20}
persona3 = {'Nombre': 'Maria', 'Edad': 30} 

ingreso_club(persona1)
ingreso_club(persona2)
ingreso_club(persona3)