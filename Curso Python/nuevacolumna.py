import csv

filePath = 'D:\\Platzi\\PROGRAMACION\\Curso Python\\products.csv'
filePathUpdated = 'D:\\Platzi\\PROGRAMACION\\Curso Python\\products_updated.csv'

with open(filePath, 'r') as file:
    leerArchivo = csv.DictReader(file)
    fieldNames = leerArchivo.fieldnames + ['price_with_iva'] + ['total_value'] + ['total_value_with_iva'] + ['amortization']
    
    with open(filePathUpdated, 'w', newline='') as updatedFile:
        escribirArchivo = csv.DictWriter(updatedFile, fieldnames=fieldNames)
        escribirArchivo.writeheader()
        
        for row in leerArchivo:
            # Calcular el precio con IVA (precio * 1.19)
            row['price_with_iva'] = float(row['price']) * 1.19
                
            # Calcular el valor total sin IVA (price * quantity)
            row['total_value'] = float(row['price']) * int(row['quantity'])
            
            # Calcular el valor total con IVA (price_with_iva * quantity)
            row['total_value_with_iva'] = row['price_with_iva'] * int(row['quantity'])
            
            # amortization = total_value_with_iva - total_value
            row['amortization'] = row['total_value_with_iva'] - row['total_value']
            
            # Escribir la fila actualizada con las nuevas columnas
            escribirArchivo.writerow(row)
