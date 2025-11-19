def triangulo_equilatero(lado, caracter):
    """
    Dibuja un triángulo equilátero con el carácter especificado.

    :param lado: Longitud del lado del triángulo.
    :param caracter: Carácter con el que se dibuja el triángulo.
    """
    for i in range(lado):
        espacios = ' ' * (lado - i - 1)
        caracteres = caracter * (2 * i + 1)
        print(espacios + caracteres)
        
def triangulo(lado, caracter):
    for i in range(lado):
        print(caracter * (i + 1))

# Ejemplo de uso
lado = int(input("Ingrese la longitud del lado del triángulo: "))
caracter = input("Ingrese el carácter para dibujar el triángulo: ")
print("Triángulo equilátero:\n")
triangulo_equilatero(lado, caracter)
print("\n")
print("Triángulo rectángulo:\n")
triangulo(lado, caracter)