from collections import Counter
import requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

csv = requests.get(url).text
linhas = csv.splitlines()

colunas_marca = []
colunas_venda = []
genero_acao = []
genero_tiro = []
genero_plaforma  = []
sem_data_lanc = []

dicionario_genero_tiro = {}
dicionario_acao = {}
dicionario_genero_plaforma  = {}

for i in range(1, len(linhas) - 1):  # faz a lista com os 3 tipos que pede pra procurar coisas
    coluna = linhas[i].split(',')
    if coluna[2] == '2009' or coluna[2] == '2010' or coluna[2] == '2011' or coluna[2] == '2012' or coluna[
        2] == '2013' or coluna[2] == '2014' or coluna[2] == '2015' or coluna[2] == '2016' or coluna[2] == '2017' or \
            coluna[2] == '2018' or coluna[2] == '2019':
        if 'Action' in linhas[i]:
            genero_acao.append(linhas[i])
        elif 'Shooter' in linhas[i]:
            genero_tiro.append(linhas[i])
        elif 'Platform' in linhas[i]:
            genero_plaforma .append(linhas[i])

for i in genero_tiro:
    coluna = i.split(',')
    chave = coluna[4]
    if coluna[7] == 'Activision':
        valor = float(coluna[8])
    else:
        valor = float(coluna[7])
    if chave in dicionario_genero_tiro:
        dicionario_genero_tiro[chave] += valor
    else:
        dicionario_genero_tiro[chave] = valor

for i in genero_acao:
    coluna = i.split(',')
    chave = coluna[4]
    if coluna[7] == 'Activision':
        valor = float(coluna[8])
    else:
        valor = float(coluna[7])
    if chave in dicionario_acao:
        dicionario_acao[chave] += valor
    else:
        dicionario_acao[chave] = valor

for i in genero_plaforma :
    coluna = i.split(',')
    chave = coluna[4]
    if coluna[7] == 'Activision':
        valor = float(coluna[8])
    else:
        valor = float(coluna[7])
    if chave in dicionario_genero_plaforma :
        dicionario_genero_plaforma [chave] += valor
    else:
        dicionario_genero_plaforma [chave] = valor

contador_genero_tiro = Counter(dicionario_genero_tiro).most_common(3)
contador_açao = Counter(dicionario_acao).most_common(3)
contador_genero_plaforma  = Counter(dicionario_genero_plaforma ).most_common(3)

print('Maiores vendas em jogos de genero_tiro:')
for x in range(len(contador_genero_tiro)):
    print(x + 1, 'º', contador_genero_tiro[x][0], ':', '%.2f em vendas' % contador_genero_tiro[x][1])

print('\nMaiores vendas em jogos de ação:')
for x in range(len(contador_açao)):
    print(x + 1, 'º', contador_açao[x][0], ':', '%.2f em vendas' % contador_açao[x][1])

print('\nMaiores vendas em jogos de genero_plaforma:')
for x in range(len(contador_genero_plaforma )):
    print(x + 1, 'º', contador_genero_plaforma [x][0], ':', '%.2f em vendas' % contador_genero_plaforma [x][1])
