def calcular_potencia(base, expoente):
    potencia = 1
    contador = 0
    for indice in range(expoente):
        potencia = potencia * base
        contador += 1
    print('O resultado da potência é:', potencia)

entrada_base = int(input('Digite o valor da base:'))
entrada_expoente = int(input('Digite o valor do expoente:'))

calcular_potencia(entrada_base, entrada_expoente)

