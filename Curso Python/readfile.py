
#Leer linea por linea
"""with open('D:\Platzi\PROGRAMACION\Curso Python\Caperucita roja.txt', 'r') as file:
    for lineas in file: 
        print(lineas.strip())"""

#Leer todas las lineas en una lista 
"""with open('D:\Platzi\PROGRAMACION\Curso Python\Caperucita roja.txt', 'r') as file:
    lineas = file.readlines()
    print(lineas)"""
    
#Agrega texto al final del documento con el uso de la letra 'a'
"""with open('D:\Platzi\PROGRAMACION\Curso Python\Caperucita roja.txt', 'a', encoding='utf-8') as file:
    file.write("\n\nEscrito por: ChatGPT")"""
    
#Sobreescribe el archivo 
with open('D:\Platzi\PROGRAMACION\Curso Python\Caperucita roja.txt', 'w', encoding='utf-8') as file:
    file.write("\n\nEscrito por: ChatGPT")
