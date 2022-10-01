def ler_entrada():
    entrada = int(input('Digite um número inteiro:'))
    return entrada

numeros_inteiros = (ler_entrada(), ler_entrada(), ler_entrada())

numeros_inteiros = sorted(numeros_inteiros)

print('Números inteiros na ordem crescente:', numeros_inteiros)