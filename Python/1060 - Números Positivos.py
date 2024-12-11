contador = 0

for i in range(6):
    valor = float(input())  
    if valor > 0:  
        contador += 1  

print(f"{contador} valores positivos")
