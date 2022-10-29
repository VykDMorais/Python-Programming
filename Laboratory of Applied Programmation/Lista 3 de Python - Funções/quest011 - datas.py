def dataExt (data):
    meses = [(), ['Janeiro', 31], ['Fevereiro', 29], ['Março', 31], ['Abril', 30], ['Maio', 31], ['Junho', 30], ['Julho', 31], ['Agosto', 31], ['Setembro', 30],['Outubro', 31], ['Novembro', 30], ['Dezembro', 31]]
    data = data.split('/')
    dia, mes, ano = int(data[0]), int (data[1]), int(data[2])
    if mes == 2:
        meses[mes][1] = bissexto(ano)
    if 0 < mes < 13 and 0 < dia <= meses[mes][1]:
        print(f"{dia} de {meses[mes][0]} de {ano}")
    else:
        print ("NULL")
def bissexto (ano):
    if ano%400 == 0 or (ano%4 == 0 and ano%100 != 0):
        return (29)
    else: 
        return 28
data = input ("Digite uma data por barras: ")
dataExt (data)
input ()