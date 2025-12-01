def sumaNumerosNaturales (n):
    
    if n == 0:
        return 0
    elif n > 0:
        return n + sumaNumerosNaturales(n-1)

print(sumaNumerosNaturales(100))
print(sumaNumerosNaturales(50))
print(sumaNumerosNaturales(500))
print(sumaNumerosNaturales(500))
print(sumaNumerosNaturales(5))
