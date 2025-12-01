import math
import sys

# Ajustar el límite de dígitos permitidos
sys.set_int_max_str_digits(500000)  # Puedes aumentar este valor según tus necesidades

def factorial_con_math(n):
    try:
        return math.factorial(n)
    except (ValueError, OverflowError) as e:
        return str(e)

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial_recursivo(n - 1)
    else:
        return "El factorial no está definido para números negativos."

n = int(input("Ingresar número para calcular su factorial: "))
"""
print("Funcion factorial con ciclo:", factorial_iterativo(n))
print("Funcion recursiva:", factorial_recursivo(n))
"""
print("Funcion math:", factorial_con_math(n))
