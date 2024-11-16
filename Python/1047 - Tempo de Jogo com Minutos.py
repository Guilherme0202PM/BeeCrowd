hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Converter horas e minutos para minutos totais
inicio_total = hora_inicial * 60 + minuto_inicial
final_total = hora_final * 60 + minuto_final

# Calcular a duração total em minutos
if final_total > inicio_total:
    duracao_total = final_total - inicio_total
else:
    duracao_total = (24 * 60 - inicio_total) + final_total

# Converter a duração total de minutos para horas e minutos
duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
