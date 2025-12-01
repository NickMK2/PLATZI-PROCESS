suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a, b: a / b

a = float(input())
b = float(input())

print("Suma:")
print(suma(a,b))
print("Resta:")
print(resta(a,b))
print("Multiplicacion:")
print(multiplicacion(a,b))
print("Division:")
print(division(a,b))

numeros = range(5)

elevadoN = list(map(lambda x: x**2, numeros))
print("Cuadrados:",elevadoN)

#Pares

pares = list(filter(lambda x: x%2 == 0, numeros))
print("Pares:", pares)