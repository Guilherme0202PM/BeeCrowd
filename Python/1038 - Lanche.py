codigo, quantidade = map(int, input().split())

# Dicionário com os preços dos itens
precos = {
    1: 4.00,  # Cachorro quente
    2: 4.50,  # X-Salada
    3: 5.00,  # X-Bacon
    4: 2.00,  # Torrada Simples
    5: 1.50   # Refrigerante
}

total = precos[codigo] * quantidade

print(f"Total: R$ {total:.2f}")
