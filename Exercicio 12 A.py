import requests
from bs4 import BeautifulSoup

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

for tabela in soup.find_all('div', class_='tabela'):
    print(tabela.text)



