valores = list(map(int, input().split()))

# Copiar os valores originais para outra lista
valores_originais = valores[:]

# Ordenar valores
valores.sort()

# Imprimir os valores ordenados
for valor in valores:
    print(valor)

print()

# Imprimir os valores originais
for valor in valores_originais:
    print(valor)
