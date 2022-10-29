relatorio = []
contador = []
def valorPagamento (valor, atraso):
    if atraso == 0:
        print(f"O valor a ser pago é: {valor}")
        relatorio.append (valor)
        contador.append (1)  
    elif atraso > 0:
        valor = valor + (valor*0.03) + (valor*atraso*0.001)
        print(f"O valor a ser pago é: {valor}")
        relatorio.append (valor)
        contador.append (1)
    else: 
        print("Valor de prestação inválido")
while (True):
    valor = float(input("Qual o valor da prestação? "))
    atraso = int(input("Qual é o atraso, em dias? "))
    encerra = int(input("Se quiser encerrar o programa, digite 0: "))
    valorPagamento (valor, atraso)
    if encerra == 0:
        break
print (f"O número de prestacões pagas foi: {sum(contador)}. O valor total foi de: {sum(relatorio)} ")
input()