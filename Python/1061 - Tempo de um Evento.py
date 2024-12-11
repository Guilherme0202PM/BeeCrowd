diaInicio = int(input().split()[1])  # Extrai o dia de início
horaInicio, minutoInicio, segundoInicio = map(int, input().split(" : "))  # Extrai hora, minuto e segundo de início

dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))

# Converte tudo para segundos
inicio_segundos = diaInicio * 86400 + horaInicio * 3600 + minutoInicio * 60 + segundoInicio
fim_segundos = dia_fim * 86400 + hora_fim * 3600 + minuto_fim * 60 + segundo_fim

duracao_segundos = fim_segundos - inicio_segundos

# Converte a duração de segundos para dias, horas, minutos e segundos
dias = duracao_segundos // 86400
duracao_segundos %= 86400
horas = duracao_segundos // 3600
duracao_segundos %= 3600
minutos = duracao_segundos // 60
segundos = duracao_segundos % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
