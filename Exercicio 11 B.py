from collections import Counter
import requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

csv = requests.get(url).text

linhas = csv.splitlines()
lista_marcas = []
lista_vendas = []
tipo_jogos = []

for i in range(1, len(linhas) - 1):
    if 'Action' in linhas[i]:
        tipo_jogos.append(linhas[i])
    elif 'Shooter' in linhas[i]:
        tipo_jogos.append(linhas[i])
    elif 'Platform' in linhas[i]:
        tipo_jogos.append(linhas[i])
for j in range(1, len(tipo_jogos) - 1):
    coluna = tipo_jogos[j].split(',')
    lista_marcas.append(coluna[4])
    lista_vendas.append(coluna[9])

for i in range(len(lista_vendas)):
    lista_vendas[i] = float(lista_vendas[i])
dic = dict(zip(lista_marcas, lista_vendas))

for g in tipo_jogos:
    coluna = g.split(',')
    palavra = coluna[4]
    valor = float(coluna[9])
    if palavra in dic:
        valor_antigo = dic[palavra]
        valor_novo = valor_antigo + valor
        dic[palavra] = valor_novo

contador = Counter(dic).most_common(3)

for x in range(len(contador)):
    print(x + 1,' - ',contador[x][0],':', '%.2f em vendas' % contador[x][1])

