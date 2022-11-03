def conversor (hora):
    b = hora/12
    if b == 1:
        print (f"O horáio é 12:{minuto} PM")
    elif b > 1 and b < 2:
        print (f"O horário é {hora - 12}:{minuto} PM")
    elif b >= 0 and b < 1:
        print (f"O horário é {hora}:{minuto} AM")
    else:
        print("Erro, número de horas inválido")
while (True):
    hora = int(input("Qual a hora? "))
    minuto = int(input("Qual o minuto? "))
    if minuto >= 0 and minuto < 60:
        conversor (hora)
    else:
        print("Erro, número de minutos inválido")
    continua = input("Se quiser parar o programa, digite 0: ")
    if continua == 0:
        break
input()
