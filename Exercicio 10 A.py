import requests

url="https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

requisicao = requests.get(url, timeout=5)
if requisicao.status_code != 200:
    requisicao.raise_for_status()
else:
    print("Conectado com sucesso!\n")

csv = requisicao.text

linhas = csv.splitlines()

contador_suecia = 0
contador_dinamarca = 0
contador_noruega = 0

lista_ano = []

for l in range(1, len(linhas)):
    coluna = linhas[l].split(',')
    lista_ano.append(int((coluna[0])))
for i in range(1, len(linhas) - 1):
    if lista_ano[i] >= 2001:
        if 'Curling' in linhas[i] and 'SWE' in linhas[i] and 'Gold' in linhas[i]:
            contador_suecia += 1
        elif 'Skating' in linhas[i] and 'SWE' in linhas[i] and 'Gold' in linhas[i]:
            contador_suecia += 1
        elif 'Skiing' in linhas[i] and 'SWE' in linhas[i] and 'Gold' in linhas[i]:
            contador_suecia += 1
        elif 'Ice Hockey' in linhas[i] and 'SWE' in linhas[i] and 'Gold' in linhas[i]:
            contador_suecia += 1
        elif 'Curling' in linhas[i] and 'DEN' in linhas[i] and 'Gold' in linhas[i]:
            contador_dinamarca += 1
        elif 'Skating' in linhas[i] and 'DEN' in linhas[i] and 'Gold' in linhas[i]:
            contador_dinamarca += 1
        elif 'Skiing' in linhas[i] and 'DEN' in linhas[i] and 'Gold' in linhas[i]:
            contador_dinamarca += 1
        elif 'Ice Hockey' in linhas[i] and 'DEN' in linhas[i] and 'Gold' in linhas[i]:
            contador_dinamarca += 1
        elif 'Curling' in linhas[i] and 'NOR' in linhas[i] and 'Gold' in linhas[i]:
            contador_noruega += 1
        elif 'Skating' in linhas[i] and 'NOR' in linhas[i] and 'Gold' in linhas[i]:
            contador_noruega += 1
        elif 'Skiing' in linhas[i] and 'NOR' in linhas[i] and 'Gold' in linhas[i]:
            contador_noruega += 1
        elif 'Ice Hockey' in linhas[i] and 'NOR' in linhas[i] and 'Gold' in linhas[i]:
            contador_noruega += 1
if contador_suecia > contador_dinamarca and contador_suecia > contador_noruega:
    print('A Suécia é a maior medalhista de ouro. \nTotal de:', contador_suecia, 'medalhas.')
elif contador_dinamarca > contador_suecia and contador_dinamarca > contador_noruega:
    print('A Dinamarca é a maior medalhista de ouro. \nTotal de:', contador_dinamarca, 'medalhas.')
elif contador_noruega > contador_suecia and contador_noruega > contador_dinamarca:
    print('A Noruega é a maior medalhista de ouro. \nTotal de:', contador_noruega, 'medalhas.')


