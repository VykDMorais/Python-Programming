def reverso (n):
    invert = str(n)
    print (f"Inverso de {n}: {invert[::-1]}")
while (True):
    n = int(input("Digite um inteiro: "))
    encerra = int(input("Digite 0 para encerrar o programa: "))
    if encerra == 0:
        reverso (n)
        break
    else:
        reverso (n)
input()