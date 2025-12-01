#Sucesion Fibonacci
# def susecionFibonacci(n):
#     sucesionF = [0,1]
#     print('Mio: ')
#     for i in range(2,n):
#         n = sucesionF[i-1] + sucesionF[i-2]
#         sucesionF.append(n)
        
#     print(sucesionF)        
# susecionFibonacci(100)

#Fibonacci Gemini

# def fibonacci(n):
#     fib_sequence = [0, 1]  # Iniciamos la secuencia con los dos primeros valores
#     print("Gemini: ")
#     for i in range(2, n):
#         next_fib = fib_sequence[i-1] + fib_sequence[i-2]
#         fib_sequence.append(next_fib)
#     return fib_sequence

# result = fibonacci(100000)
# print(result)

#Fibonacci Gemini con Yield(MAS EFICIENTE)

def fibonacci_yield(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
    
for num in fibonacci_yield(3000):
    print(num,end=",")