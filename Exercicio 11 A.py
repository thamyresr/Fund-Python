import requests
from collections import Counter

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

csv = requests.get(url).text
linhas = csv.splitlines()
colunas = []
tipos_jogos = []

for i in range(len(linhas)):
    if 'Action' in linhas[i]:
        tipos_jogos.append(linhas[i])
    elif 'Shooter' in linhas[i]:
        tipos_jogos.append(linhas[i])
    elif 'Platform' in linhas[i]:
        tipos_jogos.append(linhas[i])
for j in range(len(tipos_jogos)):
    coluna = tipos_jogos[j].split(',')
    colunas.append(coluna[4])
contador = Counter(colunas).most_common(3)
for x in range(len(contador)):
    print(x + 1, ' - ', contador[x][0], ':', contador[x][1], 'jogos')

