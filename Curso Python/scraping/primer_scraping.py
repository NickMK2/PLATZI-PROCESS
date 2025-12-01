import beautifulsoup4 as bs
import requests

url = input('Ingrese la URL de la pagina web: ').strip()
if not url.startswith('http'):
    url = 'http://' + url
response = requests.get(url)
if response.status_code == 200:
    soup = bs.BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    print(f'Title of the page: {title}')
else:
    print(f'Error: Unable to fetch the page. Status code: {response.status_code}')

    