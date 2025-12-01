import csv

# Se crea un nuevo producto
nuevoProducto = {
    'name': 'Dildo',
    'price': 500000,
    'quantity': 5,
    'brand': 'Dolce & Gabbana',
    'category': 'Adult Toys',
    'entry_date': '02/10/2024'
}

filepath = 'D:\\Platzi\\PROGRAMACION\\Curso Python\\products.csv'

# Agrega información al final del archivo
with open(filepath, 'a', newline='', encoding='utf-8') as file:
    
    leerCsv = csv.DictWriter(file, fieldnames = nuevoProducto.keys())
    leerCsv.writerow(nuevoProducto)

# Lee la información y la muestra por consola acorde a las columnas especificadas
with open(filepath, mode='r', encoding='utf-8') as file:
    leerCsv = csv.DictReader(file)
    
    for row in leerCsv:
        print(f"Nombre: {row['name']}, Precio: {row['price']}, Cantidad: {row['quantity']}")
