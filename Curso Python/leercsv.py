import csv

#Lee la informacion y la muestra por consola acorde a las columnas especificadas
with open('D:\Platzi\PROGRAMACION\Curso Python\products_updated.csv', mode='r') as file:
    leerCsv = csv.DictReader(file)
    
    for row in leerCsv:
        print(f"Nombre: {row['name']}, Precio: {row['price']}")
