valor = float(input())

valor_em_centavos = int(round(valor * 100))

notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    quantidade_notas = valor_em_centavos // nota
    print(f"{quantidade_notas} nota(s) de R$ {nota / 100:.2f}")
    valor_em_centavos %= nota

print("MOEDAS:")
for moeda in moedas:
    quantidade_moedas = valor_em_centavos // moeda
    print(f"{quantidade_moedas} moeda(s) de R$ {moeda / 100:.2f}")
    valor_em_centavos %= moeda
