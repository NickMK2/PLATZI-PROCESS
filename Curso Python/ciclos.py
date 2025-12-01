frutas = {"Melon","Papaya","Platano","Pera","Manzana"}
numerosLista = [12, 98, 45, 32, 17, 89, 65, 73, 21, 54,
9, 38, 76, 15, 42, 87, 64, 51, 29, 0,
83, 69, 56, 43, 30, 18, 75, 92, 27, 5,
48, 35, 22, 19, 77, 94, 61, 58, 46, 33,
20, 8, 71, 96, 63, 50, 37, 24, 11, 85,
72, 59, 47, 34, 23, 10, 95, 62, 57, 44,
31, 16, 78, 93, 60, 49, 36, 25, 13, 86,
74, 67, 52, 39, 26, 14, 91, 84, 70, 55,
41, 28, 12, 97, 66, 53, 40, 27, 15, 82,
79, 68, 54, 41, 29, 17, 83, 70, 56, 43]
sucesionF = 0
texto = "Hola amiguitos"

print("Frutas:",frutas)
print("Lista de numeros:",numerosLista)

for char in texto:
    print(char)
for char in frutas:
    print(char)
for fruta in frutas:
    print(fruta)
for numero in numerosLista:
    print(numero)
print("----------------------------")
for caracter in texto:
    print(caracter)
print("----------------------------")

#Numero pares 
for numero in numerosLista:
    if numero%2 == 0:
        print("Es par:",numero)
        
#Numero impares 
for numero in numerosLista:
    if numero%2 != 0:
        print("Es impar:",numero)
    