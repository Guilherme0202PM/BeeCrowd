A, B, C = map(float, input().split())

lados = sorted([A, B, C], reverse=True)
A, B, C = lados[0], lados[1], lados[2]

# Verificar se forma um triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Verificar o tipo de triângulo
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    if A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
