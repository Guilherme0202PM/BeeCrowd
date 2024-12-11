salario = float(input())

if salario <= 2000.00:
    print("Isento")
else:
    imposto = 0.0
    if salario <= 3000.00:
        imposto += (salario - 2000.00) * 0.08
    elif salario <= 4500.00:
        imposto += (1000.00 * 0.08)  # 8% sobre os primeiros R$ 1000,00
        imposto += (salario - 3000.00) * 0.18  # 18% sobre o que exceder R$ 3000,00
    else:
        imposto += (1000.00 * 0.08)  # 8% sobre os primeiros R$ 1000,00
        imposto += (1500.00 * 0.18)  # 18% sobre os próximos R$ 1500,00
        imposto += (salario - 4500.00) * 0.28  # 28% sobre o que exceder R$ 4500,00

    print(f"R$ {imposto:.2f}")