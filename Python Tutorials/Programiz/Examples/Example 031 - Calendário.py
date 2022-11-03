import calendar
while (True):
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    if mes >= 1 and mes <= 12:
        print (calendar.month(ano, mes))
    else:
        print ("Erro, valor de mês inválido")
        break