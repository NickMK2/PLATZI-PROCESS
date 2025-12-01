# Contar cuántas líneas tiene el archivo de texto
with open('D:\Platzi\PROGRAMACION\Curso Python\Caperucita roja.txt', 'r', encoding='utf-8') as file:
    count = 0
    for linea in file:
        count += 1  # Suma 1 por cada línea
    print(f"El archivo tiene {count} líneas.")

# Contar cuántas líneas tiene el archivo de texto
with open('D:\Platzi\PROGRAMACION\Curso Python\Caperucita roja.txt', 'r', encoding='utf-8') as file:
    lineas = file.readlines()  # Lee todas las líneas en una lista
    numero_de_lineas = len(lineas)  # Cuenta el número de líneas
    print(f"El archivo tiene {numero_de_lineas} líneas.")
    print(f"Lineas {lineas}.")
