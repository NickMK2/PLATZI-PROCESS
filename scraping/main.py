import requests
from bs4 import BeautifulSoup

url = input("Ingrese la URL: ").strip()
if not url.startswith("http"):
    url = "http://" + url

response = requests.get(url)
if response.status_code != 200:
    print(f"Error al acceder a la URL: {response.status_code}")
else:
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else "No se encontró el título"
    print(f"Título de la página: {title}")

# Articulos
articulos = soup.find_all('article')
print(f"Se encontraron {len(articulos)} artículos en la página.")

# Extraer los titulos de los articulos
for i, articulo in enumerate(articulos, start=1):
    titulo = articulo.find('h2')
    if titulo:
        print(f"Artículo {i}: {titulo.get_text(strip=True)}")
    else:
        print(f"Artículo {i}: No se encontró título")

articulos_select = soup.select('.article')
print(f"Se encontraron {len(articulos_select)} artículos usando select.")
print(articulos_select)