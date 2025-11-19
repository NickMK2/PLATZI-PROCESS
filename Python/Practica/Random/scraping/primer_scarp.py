import requests
import csv
from bs4 import BeautifulSoup
import json
import time
import random

url = input('Introduce la URL: ').strip()
if not url.startswith(('http://','https://')):
    url = 'http://' + url

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# selector para los artículos
clases = "product_pod"
selector = 'article.' + '.'.join(clases.split())
articulos = soup.select(selector)

# PREPARO la lista vacía ANTES del bucle
product_list = []

for art in articulos:
    # Nombre
    nombre = art.find('h3').find('a')['title']
    # Precio
    precio = art.find('p', class_='price_color').text
    # URL de la imagen
    imagen_src = art.find('img')['src']
    imagen_url = 'https://books.toscrape.com/' + imagen_src.lstrip('../')
    # Numero de estrellas 
    estrellas = art.find('p', class_='star-rating')['class'][1]  # 'One', 'Two', etc.
    print(estrellas)
    #Disponibilidad 
    disponibilidad = art.find('p', class_='instock availability').text.strip()
    print(disponibilidad)
    # Por cada artículo creo un dict y lo añado
    product_list.append({
        'nombre': nombre,
        'precio': precio,
        'imagen_url': imagen_url,
        'estrellas': estrellas,
        'disponibilidad': disponibilidad
    })

# Ahora vuelco toda la lista al CSV
path_csv = 'productos.csv'
with open(path_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['nombre', 'precio', 'imagen_url', 'estrellas', 'disponibilidad'])
    writer.writeheader()
    writer.writerows(product_list)

print(f'Los datos se han guardado en {path_csv}')
print(f'Extracción completada: {len(product_list)} productos encontrados')
