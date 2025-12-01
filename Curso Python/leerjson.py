import json

filePath = r'D:\Platzi\PROGRAMACION\Curso Python\products.json'

nuevoProducto = {
        "name": "Lenovo Ideapad Gaming 3",
        "price": 1200,
        "quantity": 4,
        "brand": "BrandName",
        "category": "Electronics",
        "entry_date": "2024-01-05"
    }

# Leer archivo
with open(filePath, 'r') as file:
    leerArchivo = json.load(file)

leerArchivo.append(nuevoProducto)

with open(filePath, 'w') as file:
    escribirArchivo = json.dump(leerArchivo, file, indent=4)