import requests
from bs4 import BeautifulSoup
import re

url = 'http://brasil.pyladies.com/about'
palavra = 'ladies'

html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

quantidade = len(re.findall(palavra, soup.get_text()))

print('A palavra', palavra, 'apareceu no conteúdo da página:', quantidade, 'vezes.')


