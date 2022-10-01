import requests

def imprimir_relatorio(rotulo, lista, pais):
    print(pais)
    print(rotulo.replace(',', '  '))
    for i in lista:
        print(i.replace(',', ' '))
    print('\n-------------------------------------------------')

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

requisicao = requests.get(url, timeout=5)
if requisicao.status_code != 200:
    requisicao.raise_for_status()
else:
    print("Conectado com sucesso!")

csv = requisicao.text
linhas = csv.splitlines()

rotulo = linhas[0]
suecia = []
dinamarca = []
noruega = []
lista_ano = []

for l in range(1, len(linhas)):
    coluna = linhas[l].split(',')
    lista_ano.append(int((coluna[0])))
for i in range(1, len(linhas) - 1):
    if lista_ano[i] >= 2001:
        if 'SWE' in linhas[i]:
            suecia.append(linhas[i])
        elif 'DEN' in linhas[i]:
            dinamarca.append(linhas[i])
        elif 'NOR' in linhas[i]:
            noruega.append(linhas[i])

imprimir_relatorio(rotulo, suecia, 'Suécia')
imprimir_relatorio(rotulo, dinamarca, 'Dinamarca')
imprimir_relatorio(rotulo, noruega, 'Noruéga')
