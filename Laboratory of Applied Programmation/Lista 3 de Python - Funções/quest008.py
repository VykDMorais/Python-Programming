def contador (n):
    r = str(n)
    print (f"Tamanho de {n}: {len(r)}")
while (True):
    n = int(input("Digite um inteiro: "))
    encerra = int(input("Digite 0 para encerrar o programa: "))
    if encerra == 0:
        contador (n)
        break
    else:
        contador (n)
input()       