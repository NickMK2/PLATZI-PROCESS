lista_personas = [{"nombre": "Carla", "salario": "5000000"}
                       ,{"nombre": "Jeshid", "salario": "6000000"}
                       ,{"nombre": "Mario", "salario": "5000000"}
                       ,{"nombre": "Juan", "salario": "8000000"}]

def salario_minimo(lista_personas, salario):
    print(f"Personas con salario menor o igual a {salario}:")
    for persona in lista_personas:
        if float(persona["salario"]) >= salario:
            print(f"Nombre: {persona['nombre']}, Salario: {persona['salario']}")
    
salario_minimo(lista_personas, 4000000.0)
mi_cadena = "Python"
mi_tupla = tuple(mi_cadena)
print(mi_tupla)  # Salida: ('P', 'y', 't', 'h', 'o', 'n')
print(lista_personas[2]["nombre"])
