from bs4 import BeautifulSoup
from collections import Counter
import requests

url = 'http://brasil.pyladies.com/about/'

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
lista = []
palavras = []
to = []
for texto in soup.find_all('p', class_='about-text'):
    lista.append(texto.text)
for l in lista:
    palavra = l.split(' ')
    palavras.append(palavra)

a = len(palavras[0]) - 12
b = len(palavras[1]) - 12
c = len(palavras[2]) - 12
d = len(palavras[3]) - 12
total = (len(palavras[0][12:a])) + (len(palavras[1][12:b])) + (len(palavras[2][12:c])) + (len(palavras[3][12:d]))

print('Total de palavras:', total)
for i in palavras[0]:
    if i != '' or i != '\n' or i != '\\n':
        to.append(i)
for i in palavras[1]:
    if i != '' or i != '\n' or i != '\\n':
        to.append(i)
for i in palavras[2]:
    if i != '' or i != '\n' or i != '\\n':
        to.append(i)
for i in palavras[3]:
    if i != '' or i != '\n':
        to.append(i)

contador = Counter(to)

print('\nPalavras que só aparecem uma vez na página:')
for x in contador:
    if contador[x] == 1:
        print(' |', x, end ='')

