pesquisa = int(input(""))

mes = ["Ajuste","January", "February", "March","April","May","June","July","August","September","October","November","December"]

if 0 <= pesquisa < len(mes):
    print(mes[pesquisa])
