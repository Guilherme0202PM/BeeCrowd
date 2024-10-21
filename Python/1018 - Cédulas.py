N = int(input())

valor_inicial = N

notas = [100, 50, 20, 10, 5, 2, 1]

print(valor_inicial)

for nota in notas:
    quantidade_notas = N // nota  
    print(f"{quantidade_notas} nota(s) de R$ {nota},00")
    N %= nota  # Atualiza N para o próximo valor a ser decomposto
