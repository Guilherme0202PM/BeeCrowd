contador = 0
acumulador = 0

for i in range(6):
    valor = float(input())  
    if valor > 0:  
        acumulador = acumulador + valor
        contador += 1

media = acumulador/contador
print(f"{contador} valores positivos")
print(f"{media:.1f}")
