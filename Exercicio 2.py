calculo = 0

entrada = int(input('Digite um valor inteiro:'))

for indice in range(entrada + 1):
    if indice % 2 == 0:
        calculo = calculo + indice
print('A soma dos números pares é:', calculo)