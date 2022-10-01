import requests
from bs4 import BeautifulSoup

source = requests.get('https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html').text
soup = BeautifulSoup(source, "lxml")

regiao = soup.find_all('div', attrs={'class': 'linha'})

estado = str(input('Digite a sigla do estado da região Centro-Oeste que deseja obter informções: '))
if estado == 'DF' or estado == 'df':
    print(regiao[0].text)
elif estado == 'GO' or estado == 'go':
    print(regiao[1].text)
elif estado == 'MT' or estado == 'mt':
    print(regiao[2].text)
elif estado == 'MS' or estado == 'ms':
    print(regiao[3].text)
else:
    print('Sigla Inexistente')
