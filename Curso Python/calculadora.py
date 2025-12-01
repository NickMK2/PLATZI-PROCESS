def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error, el denominador no puede ser 0"
    return a / b

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("¡Error! Debe ingresar un número")

def calculadora():
    while True:
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("¡Error! Ingrese un número válido")
            continue

        if opcion == 5:
            print("Saliendo...")
            break

        if opcion not in [1, 2, 3, 4]:
            print("Opción no válida")
            continue

        a = obtener_numero("Ingrese el primer número: ")
        b = obtener_numero("Ingrese el segundo número: ")

        print("\n" + "-"*50)
        if opcion == 1:
            print(f"Resultado: {suma(a, b)}")
        elif opcion == 2:
            print(f"Resultado: {resta(a, b)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicacion(a, b)}")
        elif opcion == 4:
            resultado = division(a, b)
            print(f"Resultado: {resultado}")
        print("-"*50)

calculadora()