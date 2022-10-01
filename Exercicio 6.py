numeros_inteiro = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

def arrumar_numeros(numeros_inteiros):
    numeros_impares = []
    numeros_pares = ()
    for indice in range(len(numeros_inteiros)):
        if numeros_inteiros[indice] % 2 == 1:
            numeros_impares.append(numeros_inteiros[indice])
        if indice % 2 == 0:
            numeros_pares += (numeros_inteiros[indice],)
    return numeros_impares, numeros_pares

calculo = arrumar_numeros(numeros_inteiro)

print('-----Números impares-----')
for indice in calculo[0]:
    print(indice)

print('-----Posições pares da tupla-----')
for indice in calculo[1]:
    print(indice)

