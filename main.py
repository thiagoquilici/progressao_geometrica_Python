# função para calcular progressão geométrica
calcular_pg = lambda x: x * 2

# lista numérica
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# mostra o resultado da pg
print(list(map(calcular_pg, numeros)))