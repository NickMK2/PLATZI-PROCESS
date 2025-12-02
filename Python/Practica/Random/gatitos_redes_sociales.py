gatitos = [{
    'nombre': 'Rolan',
    'followers': [200, 150, 300, 400, 500]
},
{
    'nombre': 'Mimi',
    'followers': [100, 200, 300, 400, 600]
},
{
    'nombre': 'Luna',
    'followers': [50, 150, 250, 350, 450]
},
{
    'nombre': 'Leo',
    'followers': [300, 400, 500, 600, 700]
},
{
    'nombre': 'Nina',
    'followers': [80, 160, 240, 320, 400]
}
]

def gatitos_mas_populares(lista_gatitos):
    # 1) Calculamos el total de seguidores por cada gatito
    totales = [sum(gato["followers"]) for gato in lista_gatitos]
    # 2) Determinamos cuál es el máximo
    maximo = max(totales)
    # 3) Recorremos lista_gatitos y totales en paralelo,
    #    y recogemos los nombres de los que empatan con el máximo
    resultado = []
    for gato, total in zip(lista_gatitos, totales):
        if total == maximo:
            resultado.append(gato["nombre"])
    return resultado

def find_famous_cat(cats):
    # 1) Calcular el total de seguidores por gato
    totals = [sum(cat["followers"]) for cat in cats]
    # 2) Averiguar el máximo
    max_total = max(totals)
    # 3) Devolver los nombres de los que empatan con ese máximo
    result = []
    for cat, total in zip(cats, totals):
        if total == max_total:
            result.append(cat["name"])
    return result
