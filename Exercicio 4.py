lista_numeros_inteiros = []
FLAG = 5

for indice in range(FLAG):
    entrada = int(input('Digite um valor inteiro:'))
    lista_numeros_inteiros.append(entrada)

lista_numeros_inteiros.reverse()

print('Lista de números inteiros na ordem inversa:', lista_numeros_inteiros)
