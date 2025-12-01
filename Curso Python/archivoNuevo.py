import csv

filepath = r"D:\Platzi\PROGRAMACION\Curso Python\nuevoArchivo.csv"

with open(filepath, "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Nombre", "Apellido", "Edad", "Genero", "Suma de edades"])
    writer.writerow(["Pedro", "Gonzalez", 20, "M"])
    writer.writerow(["Ana", "Martinez", 22, "F"])
    writer.writerow(["Juan", "Perez", 25, "M"])
    writer.writerow(["Maria", "Gomez", 30 , "F"])

#sumar las edades de los usuarios y mostrar el resultado en una columna nueva
with open(filepath, "r") as file:
    reader = csv.reader(file)
    next(reader)
    suma = 0
    for row in reader:
        suma += int(row[2])
        row.append(suma)
        print(row)
        with open(filepath, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)