# Ejemplo:
# Entrada: [1, 2, 2, 3, 4, 4, 5]
# Salida: [1, 2, 3, 4, 5]
    
def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    elementos_vistos = set()
    
    for n in lista:
        if n not in elementos_vistos:
            lista_sin_duplicados.append(n)
            elementos_vistos.add(n)
    
    return lista_sin_duplicados

entrada = [1, 2, 2, 3,3,3,3, 4, 4, 5,5,5]
conjunto = {1,1,1,1,1,2,2,2,6,6,6,6,5,5,5}
print(eliminar_duplicados(entrada))
print(conjunto)
