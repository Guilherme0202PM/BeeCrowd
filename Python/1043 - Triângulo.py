A, B, C = map(float, input().split())

if A < B + C and B < A + C and C < A + B:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Cálculo da área do trapézio
    area = ((A + B) * C) / 2

    print(f"Area = {area:.1f}")
